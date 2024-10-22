# Cold email Internship Application

<img width="421" alt="Screen Shot 2024-10-21 at 2 45 03 PM" src="https://github.com/user-attachments/assets/0690384e-71b6-45a0-afe2-1b46cf4dcc87">


## Purpose
This script's, whilst small and relatively easy has the purpose to send cold emails applying for potential internships from a given email database.

Use this responsibly and do not spam one email or one company. This is to send one email per company.

I provided a database of Finance-related companies based in the UK as an example. This comes from the LSEUBIG webpage. Use responsibly

```
git clone https://github.com/tomvlt1/Cold-email-application
```

## Guide

Before sending, customize  you HAVE to change the following variables:
    
    sender_email, 
    password,  <- This isnt your email password but one you must create within your google account settings for application use
    cv_info,  
    filename variable,
    
    you MUST change the email text in the send_internship_emails function to your own text or just change what is within the [] brackets.
    I highly recommend testing by sending it to your own email first.
    run the following command in the terminal to run the script:
    
    export OPENAI_API_KEY= "OpenAI project API key" <- enter your own API key
    then
    python application_public.py 
    
    You can change the gpt model in the generate_custom_message function to any other model or prompt you want.
