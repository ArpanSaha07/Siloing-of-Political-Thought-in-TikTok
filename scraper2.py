from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import numpy as np
import time
import video as v


# Scraper initializer
def begin_scrape(browser):
    #browser.get("https://www.tiktok.com")
    click_first_video(browser,
                      '/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div['
                      '1]/div/div[1]/div[2]/div/video',
                      '/html/body/div[1]/div[2]/div[4]/div/div[1]/div['
                      '3]/div[1]/div[2]/div/video')
    scroll_num_for_you_videos(browser)
    # scroll_for_you(browser)


def scroll_num_for_you_videos(browser):
    count = 1
    watched_videos = 0

    while count <= 100:
        time.sleep(2)
        video_info = get_video_information(browser,
                                                    '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div['
                                                   '1]/div[1]/div[1]/a[2]/span[1]/span',
                                                   '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div['
                                                   '1]/div[1]/div[2]/h4/a/div',
                                                   '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div['
                                                   '1]/div[2]/div/div[1]/div[1]/button[1]/strong',
                                                   '/html/body/div[1]/div[2]/div[4]/div/div[2]/div['
                                                   '1]/div/div[1]/div[2]/div/div[1]/div[1]/button[2]/strong',
                                                   '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div['
                                                   '1]/div[2]/div/div[1]/div[1]/button[3]/strong',
                                                   '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div['
                                                   '1]/div[2]/div[1]/div/div[1]/button',
                                                   '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div['
                                                   '1]/div[2]/div[1]/div/div[2]/div/a',
                                                   '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/p')
        video_info.save_to_csv('videos(1).csv')

        # Continue scrolling on the for you page
        webdriver.ActionChains(browser).send_keys(Keys.ARROW_DOWN).perform()

        count += 1


    with open('bot_info/bots.json', 'r') as file:
        bots_data = json.load(file)

    bots_data['botA6']['watch_num'][0] += count

    with open('bot_info/bots.json', 'w') as file:
        json.dump(bots_data, file, indent=4)


# Main function to perform scraping functionality at for you page
def scroll_for_you(browser):
    # print("************************************* Scrolling For You *************************************************")
    time.sleep(1)
    try:
        # Hover over video to get duration
        video = browser.find_element(By.XPATH,
                                     '/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/div/video')
        ActionChains(browser).move_to_element(video).perform()
        time.sleep(1)
        duration = ''
        try:
            duration = get_browser_element_text(browser.find_element(By.XPATH,
                                                                '/html/body/div[1]/div[2]/div[4]/div/div[1]/div['
                                                                '3]/div[2]/div[2]'))
        except NoSuchElementException:
            print("Video duration not found")
        
        if len(duration) > 0:
            # Get duration of video in seconds
            duration = duration.split('/')[1]
            m, s = duration.split(':')
            duration_sec = int(m) * 60 + int(s)

            try:
                # Get bot interests
                with open('bot_info/bots.json', 'r') as f:
                    bots_data = json.load(f)
                bot_interests = bots_data['botA6']['interests']

                video_info = get_video_information(browser,
                                                   '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div['
                                                   '1]/div[1]/div[1]/a[2]/span[1]/span',
                                                   '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div['
                                                   '1]/div[1]/div[2]/h4/a/div',
                                                   '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div['
                                                   '1]/div[2]/div/div[1]/div[1]/button[1]/strong',
                                                   '/html/body/div[1]/div[2]/div[4]/div/div[2]/div['
                                                   '1]/div/div[1]/div[2]/div/div[1]/div[1]/button[2]/strong',
                                                   '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div['
                                                   '1]/div[2]/div/div[1]/div[1]/button[3]/strong',
                                                   '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div['
                                                   '1]/div[2]/div[1]/div/div[1]/button',
                                                   '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div['
                                                   '1]/div[2]/div[1]/div/div[2]/div/a',
                                                   '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/p')

                # Define probability of watching videos of other topics
                watch_other = np.random.choice([True, False], p=[0.1, 0.9], size=1, replace=False)[0]

                # Watch video, perform action, and save information to file
                if (video_info.creator in bot_interests['creators'] or any(
                        tag in video_info.tags for tag in bot_interests['tags']) or watch_other) and duration_sec < 90:
                    video_info.save_to_csv('videos.csv')
                    perform_actions(browser,
                                    '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div/div['
                                    '1]/div[1]/button[1]',
                                    '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div/div['
                                    '1]/div[1]/button[3]',
                                    '#app > div.css-14dcx2q-DivBodyContainer.e1irlpdw0 > div:nth-child(4) > div > '
                                    'div.css-1qjw4dg-DivContentContainer.e1mecfx00 > '
                                    'div.css-1stfops-DivCommentContainer.ekjxngi0 > div > '
                                    'div.css-1xlna7p-DivProfileWrapper.ekjxngi4 > '
                                    'div.css-hlg65e-DivMainContent.e1mecfx01 > div > '
                                    'div.css-1452egd-DivFlexCenterRow-StyledWrapper.ehlq8k32 > div:nth-child(1) > '
                                    'button:nth-child(3) > span > svg'
                                    )
                    time.sleep(duration_sec)
                    bots_data['botA5']['watch_num'][0] += 1
                    
                bots_data['botA5']['watch_num'][1] += 1
                print(bots_data['botA5']['watch_num'][1])

                # Write the updated data back to the JSON file
                with open('bot_info/bots.json', 'w') as f:
                    json.dump(bots_data, f, indent=4)

            except FileNotFoundError:
                print('File not found')
        else:
            print("Duration not found")

    except NoSuchElementException:
        print('Did not properly execute for you scraping script')

    # Choose what page to visit next
    page = np.random.choice(['for_you', 'search'], p=[0.76, 0.24], size=1, replace=False)[0]

    if page == 'for_you':
        # Choose if continue on current set of videos, or refresh page
        refresh = np.random.choice([True, False], p=[0.05, 0.95], size=1, replace=False)[0]

        if refresh:
            # Refresh - restart the scrolling for you scraping algorithm
            browser.get("https://www.tiktok.com/foryou")
            click_first_video(browser,
                              '/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div['
                              '1]/div/div[1]/div[2]/div/video',
                              '/html/body/div[1]/div[2]/div[4]/div/div[1]/div['
                              '3]/div[1]/div[2]/div/video')
            scroll_for_you(browser)
        else:
            # Continue scrolling on the for you page
            webdriver.ActionChains(browser).send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(1)
            scroll_for_you(browser)
    else:
        search(browser)


def search(browser):
    # print("******************************************* Searching ***************************************************")

    # Return to initial page
    global interest
    browser.get("https://www.tiktok.com/foryou")
    time.sleep(2)

    try:
        # Get bot interests
        with open('bot_info/bots.json', 'r') as f:
            bots_data = json.load(f)
        bot_interests = bots_data['botA6']['interests']

        # Choose a random interest to search
        interest_type = np.random.choice(['creators', 'tags'], p=[0.5, 0.5], size=1, replace=False)[0]
        interest = np.random.choice(bot_interests[interest_type], size=1, replace=False)[0]
    except FileNotFoundError:
        print('File not found')

    try:       
        # Write the content on the search bar and click the button
        browser.find_element(By.XPATH, '//input[contains(@type,"search")]').send_keys(interest)
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/form/button').click()

        click_first_video(browser,
                          '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div[3]/div[1]/div/div/a',
                          '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div[3]/div[1]/div['
                          '2]/div/video')
        watch_search_video(browser)

    except NoSuchElementException:
        print('Did not properly execute search scrolling script')

    search_application_flow(browser)


def scroll_search(browser):
    # print("***************************************** Scroll Search *************************************************")

    # Hover over video to charge duration
    video = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div[3]/div['
                                           '1]/div[2]/div/video')
    ActionChains(browser).move_to_element(video).perform()
    time.sleep(1)

    # Watch next video in the search results
    webdriver.ActionChains(browser).send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(1)
    watch_search_video(browser)
    search_application_flow(browser)


def search_application_flow(browser):
    # Choose what page to visit
    page = np.random.choice(['for_you', 'search'], p=[0.76, 0.24], size=1, replace=False)[0]

    if page == 'search':
        search_action = np.random.choice(['scroll', 'search'], p=[0.7, 0.3], size=1, replace=False)[0]

        if search_action == 'scroll':
            # Continue scrolling on current search results
            scroll_search(browser)
        else:
            search(browser)
    else:
        browser.get("https://www.tiktok.com/foryou")
        click_first_video(browser,
                          '/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div['
                          '1]/div/div[1]/div[2]/div/video',
                          '/html/body/div[1]/div[2]/div[4]/div/div[1]/div['
                          '3]/div[1]/div[2]/div/video')
        scroll_for_you(browser)


def watch_search_video(browser):
    duration = ''
    try: 
        duration = get_browser_element_text(browser.find_element(By.XPATH,
                                                             '/html/body/div[1]/div[2]/div[2]/div/div[2]/div['
                                                             '3]/div/div[1]/div[3]/div[2]/div[2]'))
    except NoSuchElementException:
        print("Search video duration not found")

    if len(duration) > 0:
        # Clean duration string
        duration = duration.split('/')[1]
        m, s = duration.split(':')

        video_info = get_video_information(browser,
                                           '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div['
                                           '1]/div/div[1]/div[1]/div[1]/a[2]/span[1]/span[1]',
                                           '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div['
                                           '1]/div/div[1]/div[1]/div[2]/h4/a/div',
                                           '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div['
                                           '1]/div/div[1]/div[2]/div/div[1]/div[1]/button[1]/strong',
                                           '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div['
                                           '1]/div/div[1]/div[2]/div/div[1]/div[1]/button[2]/strong',
                                           '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div['
                                           '1]/div/div[1]/div[2]/div/div[1]/div[1]/button[3]/strong',
                                           '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[2]/div['
                                           '1]/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/button',
                                           '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div['
                                           '1]/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/a',
                                           '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[5]/div/div[2]/div['
                                           '1]/div/div[1]/div[2]/div/div[2]/p')
        video_info.save_to_csv('videos.csv')

        perform_actions(browser,
                        '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div['
                        '1]/div[2]/div/div[1]/div[1]/button[1]',
                        '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div['
                        '1]/div[2]/div/div[1]/div[1]/button[3]',
                        '#tabs-0-panel-search_top > div:nth-child(3) > div > '
                        'div.css-1qjw4dg-DivContentContainer.e1mecfx00 > '
                        'div.css-1stfops-DivCommentContainer.ekjxngi0 > div > '
                        'div.css-1xlna7p-DivProfileWrapper.ekjxngi4 > div.css-hlg65e-DivMainContent.e1mecfx01 > '
                        'div > div.css-1452egd-DivFlexCenterRow-StyledWrapper.ehlq8k32 > div:nth-child(1) > '
                        'button:nth-child(3) > span > svg')

        # Watch video
        time.sleep(int(m) * 60 + int(s))
        
        with open('bot_info/bots.json', 'r') as f:
            bots_data = json.load(f)
        bots_data['botA5']['watch_num'][0] += 1
        bots_data['botA5']['watch_num'][1] += 1

        # Write the updated data back to the JSON file
        with open('bot_info/bots.json', 'w') as f:
            json.dump(bots_data, f, indent=4)
    else:
        print("Duration was not found")


def click_first_video(browser, first_video_xpath, video_xpath):
    time.sleep(5)
    try:
        # Click first video in feed
        browser.find_element(By.XPATH, first_video_xpath).click()
        time.sleep(1)

        # Hover over video to charge duration bar
        ActionChains(browser).move_to_element(browser.find_element(By.XPATH, video_xpath)).perform()
        time.sleep(1)
    except NoSuchElementException:
        print("Not able to click first video of feed")


def get_video_information(browser, creator_xpath, music_xpath, likes_xpath, comments_xpath, saved_xpath, more_xpath,
                          tags_xpath, video_url_xpath):
    # Get html elements of the video's meaningful characteristics
    creator = get_browser_element_text(browser.find_element(By.XPATH, creator_xpath))
    music = get_browser_element_text(browser.find_element(By.XPATH, music_xpath))
    likes = get_browser_element_text(browser.find_element(By.XPATH, likes_xpath))
    comments = get_browser_element_text(browser.find_element(By.XPATH, comments_xpath))
    saved = get_browser_element_text(browser.find_element(By.XPATH, saved_xpath))
    video_url = get_browser_element_text(browser.find_element(By.XPATH, video_url_xpath))

    # Expand tags if necessary, and get the text in each one of them
    expand_tags(browser, more_xpath)
    tags_div = browser.find_elements(By.XPATH, tags_xpath)
    tags = []
    for tag in tags_div:
        tags.append(get_browser_element_text(tag))

    return v.Video(creator, music, likes, comments, saved, tags, datetime.now(), video_url)


def expand_tags(browser, more_xpath):
    try:
        # Click the more... button to get the rest of the tags
        browser.find_element(By.XPATH, more_xpath).click()
        time.sleep(1)
    except ElementNotInteractableException:
        return


# Performs actions such as like and save
def perform_actions(browser, like_xpath, save_xpath, save_svg_xpath):
    # Get html elements for the clickable like and save buttons
    like_button = browser.find_element(By.XPATH, like_xpath)
    save_button = browser.find_element(By.XPATH, save_xpath)
    save_svg = browser.find_element(By.CSS_SELECTOR, save_svg_xpath)

    # Choose if the action is going to be performed
    like_prob = np.random.choice([True, False], p=[0.59, 0.41], size=1, replace=False)[0]
    save_prob = np.random.choice([True, False], p=[0.38, 0.62], size=1, replace=False)[0]

    try:
        # Like the video
        if like_prob and like_button.get_attribute("aria-pressed") == 'false':
            like_button.click()

        # Save the video
        if save_prob and save_svg.value_of_css_property("color") == 'rgba(255, 255, 255, 0.9)':
            save_button.click()
    except NoSuchElementException:
        print('Not able to perform actions in the video')


def get_browser_element_text(element):
    try:
        return element.text
    except NoSuchElementException:
        return ''
