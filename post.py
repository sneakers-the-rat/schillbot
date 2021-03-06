import logging
import os
import random
import time
import traceback
import json

import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import pdb

# thing to make work w cron
#https://bugs.chromium.org/p/chromedriver/issues/detail?id=2470
#os.environ["DISPLAY"]=":99"


###################
# post

# load credentials
with open('creds.json', 'r') as cf:
    creds = json.load(cf)


class URL:
    TWITTER = 'http://twitter.com'
    TWITTER_HOME = 'https://twitter.com/home'

class Constants:
    USERNAME = creds['USER']
    PASSWORD = creds['PASS']
    GLOBAL_ENTRY_Q = '#globalentry'


class TwitterLocator:
    # login stuff
    login_btn        = (By.CLASS_NAME, "StaticLoggedOutHomePage-buttonLogin")
    username         = (By.CLASS_NAME, "js-username-field")
    password         = (By.CLASS_NAME, "js-password-field")

    # tweet stuff
    #outer_tweet_box  = (By.CLASS_NAME, 'public-DraftStyleDefault-block')
    outer_tweet_box  = (By.CLASS_NAME, 'DraftEditor-root')
    tweet_box        = (By.CLASS_NAME, "public-DraftEditor-content")
    tweet_btn        = (By.XPATH, "//*[@data-testid='toolBar']//div[2]//div[3]")

    # poll stuff
    poll_btn         = (By.XPATH, '//div[@aria-label="Add poll"]')
    option_one       = (By.NAME, 'Choice1')
    option_two       = (By.NAME, 'Choice2')

    # etc.
    search_input     = (By.ID, "search-query")
    like_btn         = (By.CLASS_NAME, "HeartAnimation")
    latest_tweets    = (By.PARTIAL_LINK_TEXT, 'Latest')


class PollBot(object):

    def __init__(self):
        self.locator_dictionary = TwitterLocator.__dict__
        self.options = Options()
        self.options.binary_location = '/usr/bin/google-chrome'
        #self.options.add_argument("start-maximized"); #// open Browser in maximized mode
        self.options.add_argument("disable-infobars"); #// disabling infobars
        #self.options.add_argument("--disable-extensions"); #// disabling extensions
        #self.options.add_argument("--disable-gpu"); #// applicable to windows os only
        self.options.add_argument("--disable-dev-shm-usage"); #// overcome limited resource problems
        self.options.add_argument("--no-sandbox"); #// Bypass OS security model
        self.options.add_argument("--headless")
        # twitter's shit is too responsive and hides tweet box when window is small
        self.options.add_argument("--window-size=1920,1080")
        # debugging DevToolsActivePort file doesn't exist
        #self.options.add_argument("--disable-gpu")


        self.browser = webdriver.Chrome(options=self.options)  # export PATH=$PATH:/path/to/chromedriver/folder
        self.browser.get(URL.TWITTER)
        self.timeout = 2

    def login(self, username=Constants.USERNAME, password=Constants.PASSWORD):
        self.login_btn.click()
        time.sleep(1)
        self.username.click()
        time.sleep(0.1)
        self.username.send_keys(username)
        time.sleep(0.1)
        self.password.click()
        time.sleep(0.1)
        self.password.send_keys(password)
        time.sleep(0.1)
        self.browser.find_elements_by_css_selector(".clearfix>.submit")[0].click()
        time.sleep(0.5)
        self.browser.get(URL.TWITTER_HOME)
        time.sleep(0.5)

    def tweet_poll(self, post_text):

        # click the tweet box
        self.outer_tweet_box.click()
        time.sleep(1)

        # type the tweet
        self.tweet_box.send_keys('\"' + post_text.lower() + '\" uohellno.com')
        time.sleep(1)

        # make the poll
        self.poll_btn.click()
        time.sleep(0.1)
        self.option_one.click()
        time.sleep(0.1)
        self.option_one.send_keys('human schill')
        time.sleep(0.1)
        self.option_two.click()
        time.sleep(0.1)
        self.option_two.send_keys('robot schill')
        time.sleep(0.2)

        # send the tweet
        self.tweet_btn.click()
        time.sleep(2)

    def search(self, q=Constants.GLOBAL_ENTRY_Q):
        self.search_input.send_keys(q)
        self.search_input.send_keys(Keys.ENTER)

    def view_latest_tweets(self):
        self.latest_tweets.click()

    def like_tweet(self):
        tweets = self.browser.find_elements(*self.locator_dictionary['tweets'])
        tweet = random.choice(tweets)
        like = tweet.find_element(*self.locator_dictionary['like_btn'])
        like.click()
        print("Liked Tweet: {}".format(tweet.text))

    def _find_element(self, *loc):
        return self.browser.find_element(*loc)

    def __getattr__(self, what):
        try:
            if what in self.locator_dictionary.keys():
                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.presence_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()

                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.visibility_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()
                # I could have returned element, however because of lazy loading, I am seeking the element before return
                return self._find_element(*self.locator_dictionary[what])
        except AttributeError:
            super(PollBot, self).__getattribute__("method_missing")(what)


    def run(self, post_text):
        self.login()
        self.tweet_poll(post_text)
        self.browser.quit()


if __name__ == "__main__":

    ##################
    # log
    logger = logging.getLogger('main')
    log_handler = logging.FileHandler('schillbot_log.txt')
    log_formatter = logging.Formatter("%(asctime)s %(levelname)s : %(message)s")

    log_handler.setFormatter(log_formatter)
    logger.addHandler(log_handler)
    logger.setLevel(logging.INFO)
    logger.info("logging started")

    # text
    # find any new text
    with open('new_generated.txt', 'r') as genf:
        new_gen = [g.strip('\n') for g in genf.readlines()]
        if len(new_gen)>0:
            logger.info('loaded new generated quotes:\n\n{}'.format(new_gen))
    # clear file
    open('new_generated.txt', 'w').close()

    with open('new_real.txt', 'r') as realf:
        new_real = [r.strip('\n') for r in realf.readlines()]
        if len(new_real)>0:
            logger.info('loaded new generated quotes:\n\n{}'.format(new_real))
    # clear file
    open('new_real.txt', 'w').close()

    # load existing text
    # gen = pd.DataFrame({'text':new_gen, 'n':[0,0]})
    # real = pd.DataFrame({'text':new_real, 'n':[0,0]})
    #
    # gen.to_csv('generated.csv')
    # real.to_csv('real.csv')

    gen = pd.read_csv('generated.csv', index_col=0)
    real = pd.read_csv('real.csv', index_col=0)

    # add any new text to data
    if any(new_gen):
        new_gen = pd.DataFrame({'text': new_gen,
                                'n': [0] * len(new_gen)})
        gen = gen.append(new_gen)

    if any(new_real):
        new_real = pd.DataFrame({'text': new_real,
                                 'n': [0] * len(new_real)})
        real = real.append(new_real)


    ###################
    # select post
    def choose_post(df):
        # find rows with minimum number of presentations,
        # sample one
        return df.loc[df.n == df.n.min(),].sample(n=1)


    #PROP_REAL = 0.0  # proportion of real posts
    PROP_REAL = real.shape[0]/float(gen.shape[0]+real.shape[0])

    do_real = False
    if np.random.rand() < PROP_REAL:
        do_real = True
        post = choose_post(real)
        # increment n

        logging.info('POSTED REAL (n={}): {}'.format(post.n.iloc[0], post.text.iloc[0]))
    else:
        post = choose_post(gen)

        logging.info('POSTED GENERATED (n={}): {}'.format(post.n.iloc[0], post.text.iloc[0]))

    #########
    # post
    bot = PollBot()
    success = False
    try:
        bot.run(post.text.iloc[0])
        logger.info('Successfully posted')
        success = True
    except:
        logger.exception("Failed to post!", exc_info=True)

    # increment post count on success
    if success:
        if do_real:
            real.loc[post.index, 'n'] += 1
        else:
            gen.loc[post.index, 'n'] += 1

    # save current tweet data
    real.to_csv('real.csv')
    gen.to_csv('generated.csv')



