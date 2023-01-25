<h1 align="center">Meme Scraper and Instagram Uploader</h1>
<p>This script is a combination of a web scraper and an Instagram uploader. It navigates to the website "imgflip.com/i/", scrapes the image and its title, saves it to the local machine, and uploads it to an Instagram account using the "instabot" library.</p>
<h2>Features</h2>
<ul>
  <li>Scrapes images and titles from "imgflip.com/i/"</li>
  <li>Saves images to local machine</li>
  <li>Uploads images to Instagram with their titles as captions</li>
  <li>Uses a logger to log the progress and any errors that may occur</li>
</ul>
<h2>Requirements</h2>
<ul>
  <li>Python 3</li>
  <li>requests</li>
  <li>bs4 (BeautifulSoup)</li>
  <li>instabot</li>
  <li>urllib3</li>
</ul>
<h2>Usage</h2>
<ol>
  <li>Install the required libraries by running <code>pip install -r requirements.txt</code> in the terminal.</li>
  <li>Replace <code>username</code> and <code>password</code> in the script with your Instagram account's username and password.</li>
  <li>Run the script by executing <code>python script.py</code> in the terminal.</li>
</ol>
<h2>Note</h2>
<ul>
  <li>The script has a delay of 5 seconds between each upload to avoid rate limiting by Instagram.</li>
  <li>If you are running this script on a loop and uploading a large number of images, make sure to use a unique image every time to avoid getting banned by Instagram.</li>
  <li>This script is for educational and testing purposes only, use it at your own risk.</li>
</ul>
