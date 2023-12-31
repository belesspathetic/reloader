{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cafd31f4-9784-4c2f-a012-b3f907e8111f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['https://www.youtube.com/@YaninaSokolova/videos', 'https://www.youtube.com/@STERNENKO/videos', 'https://www.youtube.com/@news24tvua/videos']\n",
      "['https://www.youtube.com/watch?v=xzYuN6lVHYs&t=468s', 'https://www.youtube.com/watch?v=xchllDN54II', 'https://www.youtube.com/watch?v=U41lDhRVIZY', 'https://www.youtube.com/watch?v=LI1Dka95tyw']\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter mode: 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "⚡️ЛЕЩЕНКО влип! 😡Закликає молодь до мобілізації, а сам шляється по нічних клубах. Реакція військових\n",
      "https://www.youtube.com/watch?v=xchllDN54II\n",
      "PROCESS: Video already in db. Skiping...\n",
      "Ліквідація генерала РФ. Сальдо бере Одесу, у росіян загострення про переговори\n",
      "https://www.youtube.com/watch?v=U41lDhRVIZY\n",
      "PROCESS: Video already in db. Skiping...\n",
      "🔴Захід негайно готується! / ВІЙНА Росії з НАТО: план МОСКВИ зірвали… @Musienko_channel\n",
      "https://www.youtube.com/watch?v=1LHyuiuRDN8\n",
      "https://rr4---sn-bpb5oxu-3c2y.googlevideo.com/videoplayback?expire=1701308628&ei=dJRnZd_xL-aBp-oPr9ehqAQ&ip=178.158.249.21&id=o-AJ18gTs5H0qUmOANcIws2SRd6DMuzhalyjxN_z7bG6-z&itag=22&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=bm&mm=31%2C29&mn=sn-bpb5oxu-3c2y%2Csn-3c27sn7y&ms=au%2Crdu&mv=m&mvi=4&pl=21&initcwndbps=1141250&vprv=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=812.141&lmt=1701281612983655&mt=1701286867&fvip=5&fexp=24007246&c=ANDROID_EMBEDDED_PLAYER&txp=6308224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=ANLwegAwRgIhAP1NWX-OiasZ8zED3-eD5RrlEdanfWupeQjN8_mdwAB1AiEA5EsAQ2B6ZEZwmLkVKK34u03NgNTOC4mqkh3ya0w2nwU%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAIr_d2KBwrK9AeZnGBeosoy3ot8zeQKthDntOIv-BB7_AiEA2K5AS6D6yiwPW0kSHK6fnLxSlSHazVpJ48Ibd32mWCU%3D\n",
      "https://i.ytimg.com/vi/1LHyuiuRDN8/sddefault.jpg\n",
      "SUCCESS: 🔴Захід негайно готується! / ВІЙНА Росії з НАТО: план МОСКВИ зірвали… @Musienko_channel\n",
      "ID 940282670862625\n",
      "SUCCESS: Thumb downloaded\n",
      "SUCCESS: Thumb uploaded for 🔴Захід негайно готується! / ВІЙНА Росії з НАТО: план МОСКВИ зірвали… @Musienko_channel\n",
      "alldone\n"
     ]
    }
   ],
   "source": [
    "from mod import driver\n",
    "from mod import hidden_driver\n",
    "from selenium.webdriver.common.action_chains import ActionChains\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.common.by import By\n",
    "import random\n",
    "import time\n",
    "import pytube \n",
    "import requests\n",
    "\n",
    "page_id = \"185722847947714\"\n",
    "app_secret = \"EAAJfoxBYmKcBOwElM20IGs2rvKQLfRw7hqxP5VBCDmZCh5AnLuZBVQWgr9hAGxxcUemR8mWlSnryyIE4MI3ftAiohFNZBh4tRKZCpefaKZC9M1ouEhJ3jvjfJoEsZA5AkWQxItlQ1htZBJBqSYLPZCiOAWbC9NZAd2TyUcwBUMCi3I3vPsTiZAGug0XjJs0og5PNvOlhAPa7wZD\"\n",
    "facebook_url = f\"https://graph.facebook.com/{page_id}/videos\"\n",
    "x = \"thumbnail.jpg\"\n",
    "\n",
    "\n",
    "\n",
    "def get_stream_and_thumb(link):\n",
    "    yt = pytube.YouTube(link)\n",
    "    raw_stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()\n",
    "    stream = raw_stream.url\n",
    "    thumb = yt.thumbnail_url\n",
    "    print(stream)\n",
    "    print(thumb)\n",
    "    return stream, thumb\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "def get_video_info(browser):\n",
    "    browser.implicitly_wait(10)\n",
    "    title = browser.find_element(By.ID, \"video-title-link\").text\n",
    "    link = browser.find_element(By.ID, \"video-title-link\").get_attribute(\"href\")\n",
    "    print(title)\n",
    "    print(link)\n",
    "    return title, link\n",
    "\n",
    "## C:\\Users\\bunny\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    # ch_list lines\n",
    "    with open('ch_list.txt', 'r') as file1:\n",
    "        ch_list = file1.read().splitlines()\n",
    "\n",
    "    print(ch_list)\n",
    "    \n",
    "    with open('db.txt', 'r') as file2:\n",
    "        db = file2.read().splitlines()\n",
    "\n",
    "    print(db)\n",
    "\n",
    "\n",
    "\n",
    "    \n",
    "    raw_path = r\"C:\\\\LAB\\\\trying\\\\viewbot\\\\need a bin\\\\ytbot\\\\Profile 1\"\n",
    "    choose = input(\"Enter mode:\")\n",
    "    \n",
    "    if choose == \"hidden\":\n",
    "        browser = hidden_driver(raw_path)\n",
    "    else:\n",
    "        browser = driver(raw_path)\n",
    "\n",
    "\n",
    "    for ch in ch_list:\n",
    "        browser.get(ch)\n",
    "        (title, link) = get_video_info(browser)\n",
    "        \n",
    "        if link in db:\n",
    "            print(\"PROCESS: Video already in db. Skiping...\")\n",
    "            continue\n",
    "\n",
    "        else:\n",
    "            None\n",
    "\n",
    "        browser.quit()\n",
    "\n",
    "        \n",
    "        (stream, thumb) = get_stream_and_thumb(link)\n",
    "        \n",
    "        video_data = {\n",
    "            'access_token': app_secret,\n",
    "            'title': title,\n",
    "            'file_url': stream,\n",
    "            'description': title,\n",
    "            'published': True,\n",
    "            'privacy': {\n",
    "                'value': 'EVERYONE' \n",
    "            }\n",
    "        }\n",
    "        \n",
    "        response = requests.post(facebook_url, params=video_data)\n",
    "\n",
    "        if response.status_code == 200:\n",
    "            with open('db.txt', 'a') as file2:\n",
    "                file2.write(link + \"\\n\")\n",
    "            print(f\"SUCCESS: {title}\")\n",
    "            callback = response.json()\n",
    "            if \"id\" in callback:\n",
    "                video_id = callback[\"id\"]\n",
    "                print(f\"ID {video_id}\")\n",
    "            else:\n",
    "                print(\"Not yet\")\n",
    "        \n",
    "        facebook_url_thumbnail = f\"https://graph.facebook.com/v18.0/{video_id}/thumbnails\"\n",
    "        response_thumbnail = requests.get(thumb)\n",
    "\n",
    "        if response.status_code == 200:\n",
    "            with open(x, \"wb\") as file:\n",
    "                file.write(response_thumbnail.content)\n",
    "                print(\"SUCCESS: Thumb downloaded\")\n",
    "        else:\n",
    "            print(\"FAIL: Thumb dc\")\n",
    "\n",
    "        files = {'source': (x, open(x, 'rb'))}\n",
    "        params = {\n",
    "            'access_token': app_secret,\n",
    "            'is_preferred': 'true'\n",
    "        }\n",
    "        \n",
    "        response = requests.post(facebook_url_thumbnail, params=params, files=files)\n",
    "        if response_thumbnail.status_code == 200:\n",
    "            print(f\"SUCCESS: Thumb uploaded for {title}\")\n",
    "        else:\n",
    "            print(f\"FAIL: Thumb dc ERROR: {response_thumbnail.status_code}\")\n",
    "\n",
    "    \n",
    "    \n",
    "    print(\"alldone\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d1bfd38f-0605-4fc1-8bd1-dfbaf29a9ee5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.youtube.com/watch?v=U41lDhRVIZY\n"
     ]
    }
   ],
   "source": [
    "print(link)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d11942ad-fc9c-41a9-bcd2-72153880f309",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
