# oz-CSD-detective

Oz CSD Detective is a tool designed to detect Client-Side Desync (CSD) attack vectors. It simplifies the process of scanning high-volume URLs and endpoints for CSD vectors. With Oz CSD Detective, you can scan multiple URLs quickly and easily by providing a list or a single URL. It streamlines the entire process, making vulnerability detection simple and efficient.
------------------------------------------------------------------------------------
# How it works?
- Oz CSD Detective works by carefully examining the input data for any potential Client-Side Desync (CSD) vectors. It does this by meticulously monitoring the response time of the web application when dummy content length is appended to the input. By observing how the application responds to this manipulation, Oz CSD Detective can identify any anomalies or irregularities that may indicate the presence of CSD vulnerabilities
------------------------------------------------------------------------------------
# install oz-CSD-detective

1. Clone the Repository:
git clone https://github.com/yourusername/oz-csd-detective.git

2. Install Dependencies:
pip install requests
pip install colorama

3. Run the Tool:

'''chmod +x oz_csd_detective.py'''
python oz_csd_detective.py -l urls.txt OR -u single URL 
Replace urls.txt with the path to a file containing a list of URLs you want to check for CSD vulnerabilities.

That's it! You've now installed and run Oz CSD Detective to check for CSD vulnerabilities. 
------------------------------------------------------------------------------------



