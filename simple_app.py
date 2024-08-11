from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    qa = [
        {"question": "What experience do you have with Microsoft Active Directory?", "answer": "I have extensive experience managing Active Directory environments, including user management, group policies, and overall object management"},
        {"question": "Can you explain the difference between a domain and a workgroup in Windows networking?", "answer": "A domain is a centralized network structure managed by a server (Domain Controller), while a workgroup is a decentralized network structure where each computer is managed independently."},
        {"question": "How do you troubleshoot network connectivity issues?", "answer": "To troubleshoot network connectivity issues, I start by checking the physical connections, then I verify the network configuration, and use tools like ping, tracert, and nslookup to diagnose the problem."},
        {"question": "What is a DHCP server, and how does it work?", "answer": "A DHCP server automatically assigns IP addresses to devices on a network. It reduces manual configuration and helps manage IP address allocation efficiently."},
        {"question": "What is a Group Policy Object (GPO), and how does it work?", "answer": "A GPO is a set of rules that control the working environment of user accounts and computer accounts. It is used to enforce security settings, install software, and manage user and computer configurations."},
        {"question": "What is a service account in Active Directory, and how is it used?", "answer": "A service account is a special type of account used to run services, tasks, or processes. It has permissions dedicated to the needs of the service, minimizing security risks."},
        {"question": "Can you explain the process of backing up and restoring Active Directory?", "answer": "Unfortunately I can't"},
        {"question": "What is your experience with virtualization technologies in a Microsoft environment?", "answer": "My experience with Windows virtualization is limited to using Hyper-V on my local computer to create test machines."},
        {"question": "What is your experience with Windows Server Update Services (WSUS)?", "answer": "Unfortunately, I don't have experience with Windows Server Update Services."},
        {"question": "An employee’s computer is infected with malware. What steps would you take to remove the malware and prevent future infections?", "answer": "I would isolate the computer from the network, run a full malware scan, remove the malware, and ensure that all software and operating systems are up to date. I would also educate the user on safe browsing practices. In some companies where I've worked, infected computers are reinstalled for greater security."},
        {"question": "A user reports that they are unable to access a network folder. What steps would you take to troubleshoot and resolve this issue?", "answer": "I would check the user's permissions, ensure the network path is correct, verify the network connection, and check if the folder is accessible from other devices."},
        {"question": "A critical server is running low on disk space. What steps would you take to free up space on the server and prevent this issue from recurring?", "answer": "I would identify and delete unnecessary files, such as old logs and temporary files, move large files to another storage, and consider expanding the storage capacity."},
        {"question": "A new application needs to be installed on multiple Windows computers in the network. What approach would you take to ensure a successful and efficient deployment of the application?", "answer": "I would use Group Policy or a deployment tool like System Center Configuration Manager (SCCM) to automate the installation process.This way, the process will be automated, and in companies with many employees, it's impossible to install software on each individual computer manually."},
        {"question": "A user complains that they are unable to connect to a VPN. What steps would you take to troubleshoot and resolve the issue?", "answer": "I would verify the user's account is locked, user's credentials, check the VPN server's status, ensure that the user's device is correctly configured, and check for any network issues that might be blocking the connection. "},
        {"question": "A database on a server has become corrupted, causing data loss. What steps would you take to recover the lost data and prevent similar incidents in the future?", "answer": "I would restore the database from the most recent backup, check logs and not only for errors, and ensure that regular backups are being taken."},
        {"question": "A server’s RAID array has failed, causing data loss. What steps would you take to recover the lost data and ensure that the server is back online as soon as possible?", "answer": "I would replace the failed disk(s), rebuild the RAID array if I can and review the RAID setup to ensure redundancy and reliability."},
        {"question": "An employee has left the company, and their account needs to be disabled across all systems. What steps would you take to ensure their access is revoked and data secured?", "answer": "I would immediately disable their user account, revoke any access tokens or credentials."},
        {"question": "The company needs to implement a backup and disaster recovery plan. What steps would you take to design and implement a robust backup and recovery strategy?", "answer": "I would assess the criticality of data and systems, choose appropriate backup solutions (on-site, off-site, cloud), define backup schedules, and test recovery procedures to ensure they work as expected."},
        {"question": "A network printer is experiencing connectivity issues, preventing users from printing. What steps would you take to troubleshoot and resolve the issue?", "answer": "I would check the printer's network connection, ensure it has a valid IP address, restart the print spooler service, and verify that users have the correct printer drivers installed."},
        {"question": "A server running critical applications has become unresponsive. What steps would you take to troubleshoot and resolve the issue as quickly as possible?", "answer": "I would check the server's resource usage, look for any hardware failures, review logs for errors, and consider restarting services or the server if necessary. I would also assess the impact and communicate with stakeholders."},
    ]

    template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>EnduroSAT SRE Test</title>
    </head>
    <body>
        <h1>EnduroSAT SRE Test</h1>
        <ol>
        {% for item in qa %}
            <li><strong>{{ item.question }}</strong><br>
            Answer: {{ item.answer }}<br><br></li>
        {% endfor %}
        </ol>
    </body>
    </html>
    '''
    
    return render_template_string(template, qa=qa)

if __name__ == "__main__":
    app.run(debug=True)
