import smtplib
from email.message import EmailMessage
from Includes.BaseClass import BaseClass
from Includes.Common import Common
from Logic.Admin.Elections import Elections
import threading


class Emails(BaseClass):

    def __init__(self):
        super().__init__()
        self.ensure_db()

    def send_email(self,receiver,subject,message, html = None):
        email_config = self.get_email_config()
        sender = Common.unlocker(email_config["sender_email"])
        port =int(Common.unlocker(email_config["port"]))
        password = Common.unlocker(email_config["password"])
        smtp = Common.unlocker(email_config["smtp"])


        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] =receiver
        msg.set_content(message)

        if html:
            msg.add_alternative(html, subtype='html')

        with smtplib.SMTP_SSL(smtp, port )as smtp:
            smtp.login(sender, password )
            smtp.send_message(msg)


    def change_configuration(self,sender_email,port,password,smtp):
        sender_email = Common.locker(sender_email)
        port = Common.locker(port)
        password = Common.locker(password)
        smtp = Common.locker(smtp)

        table_name = "email_config"
        data = {
            "sender_email": sender_email,
            "port": port,
            "password":password,
            "smtp": smtp
        }
        condition = "id = 1"
        self.db.update(table_name, data, condition)

    def get_email_config(self):
        query = "select sender_email,port,password,smtp from email_config;"
        results = self.db.query(query)
        print(results)
        results = results["first_row"][0]
        return results

    def build_html_table(self, candidates):
        html = """
        <html>
        <body style="background-color: #EAEAEA; font-family: 'Times New Roman', Times, serif; color: #2e3e55;">
            <h2 style="color: #2e3e55;">Election Results</h2>
            <table border="1" cellpadding="10" cellspacing="0" style="border-collapse: collapse; width: 100%; background-color: #bde4ff; color: #2e3e55;">
                <tr style="background-color: #3498db; color: white;">
                    <th>Candidate Name</th>
                    <th>Affiliation</th>
                    <th>Obtained Votes</th>
                </tr>
        """
        for candidate in candidates:
            html += f"""
                <tr>
                    <td>{Common.unlocker(candidate['candidate_name'])}</td>
                    <td>{Common.unlocker(candidate['affiliations'])}</td>
                    <td>{candidate['total_votes']}</td>
                </tr>
            """
        html += """
            </table>
        </body>
        </html>
        """
        return html


    def result_mail(self, election_id, display_id, title):
        def background_task():
            election = Elections()
            results = election.get_result(election_id)
            print(results)
            html_body = self.build_html_table(results)

            subject = f"Election Results: '{title}',(ID:{Common.unlocker(display_id)})"
            text_message = "Please find the election results below."

            for result in results:
                receiver_email = Common.unlocker(result["email"])
                self.send_email(receiver_email, subject, text_message, html=html_body)

        # Run email sending in background thread
        threading.Thread(target=background_task, daemon=True).start()

