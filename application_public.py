import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import time
from openai import OpenAI

def send_email(sender_email, receiver_email, password, subject, body):
    
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  
        server.login(sender_email, password)
        
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        
        server.quit()
        print(f"Email sent successfully to {receiver_email}! \n")
    except Exception as e:
        print(f"Error sending email to {receiver_email}: {e}")


def generate_custom_message(cv_info, company_name):
    client = OpenAI()
    prompt = (f"Based on my experience: {cv_info}, write a one or two-line statement that links my experience to the work {company_name} is doing.Make it very concise and to the point, there has to be a clear link between the statements. Your answer MUST and should be completing this sentence I am especially interested in your firm because of your focus on [industry or recent deal the company has done]. Do not hallucinate and found yourself only on what is true")
    
    try:
        completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a student seeking an internship at a high level company."},
        {
            "role": "user",
            "content": prompt
        }
    ]
)
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error generating custom message: {e}")
        return ""

def send_internship_emails(sender_email, password, recipients_df, cv_info):
    for index, row in recipients_df.iterrows():
        receiver_email = row['email']
        company_name = row['company']


        custom_message = generate_custom_message(cv_info, company_name)

        subject = f"{company_name} - [x] month internship for x Year student at x university"
        body = (f"To whom it may concern, \n\n"
                
                f"I am writing to you to see if {company_name} might be interested in taking on a summer intern with starting anytime in [x] until [x]."
                f" I am a student at [X] university studying a [x] degree with a current GPA of [x] as well having completed internships in [briefly describe the most relevant internships] \n\n"
                f"{custom_message} \n\n"
                f"If you have any availability next week, I would greatly appreciate the chance to speak with you and learn more about your firm and the possibility of completing a 2-3 month internship there. I have not attached my CV to this email to prevent it from going to spam, however, I would be very happy to provide it at your request.\n\n"
                
                
                f"Best, \n [First name last name].")

   
        sent_email = send_email(sender_email, receiver_email, password, subject, body)
        
            
        recipients_df.to_excel('test.xlsx', index=False)
        
        
        time.sleep(45)  
        
        
def main():
    """
    Main function to send emails to companies for internships
    Before sending, customize the you HAVE to change the following variables:
    
    sender_email, 
    password, 
    cv_info,  
    filename variable,
    
    you MUST change the email text in the send_internship_emails function to your own text.
    run the following command in the terminal to run the script:
    
    export OPENAI_API_KEY="OpenAI project API key"
    then
    python application_public.py 
    
    You can change the gpt model in the generate_custom_message function to any other model or prompt you want.
    
    
    """
    sender_email = "sender@gmail.com" #add your email here
    password = "password"#this isnt your email password but a password you create specifically for application within google, you can create one in your google account settings
    cv_info = """ """ #paste your WHOLE cv here and all information you think will be relevant, between the triple quotes
    filename = "test.xlxs" 
    #add the name of the file you want to read the emails and companies from. MAKE SURE IT IS FORMATTED with these labels "company" and "email" as column name. 
    #Use the example file in the git for the format
    
    recipients_df = pd.read_excel(filename)
    recipients_df = recipients_df.dropna(subset=['email'])
    recipients_df = recipients_df.dropna(subset=['company'])
    send_internship_emails(sender_email, password, recipients_df, cv_info)
    
    
main()

    
    
    