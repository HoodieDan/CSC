import requests
import matplotlib.pyplot as plt

# my api key
api_key = '?key=AIzaSyCTy4-2msz8Ru9Bru9hu7ynnw85YJI5VAc'

search_endpoint = "https://www.googleapis.com/youtube/v3/search?part=snippet&key=AIzaSyCTy4" \
                  "-2msz8Ru9Bru9hu7ynnw85YJI5VAc&regionCode=NG&type=video&q= "


def get_movies(movie_name):
    response = requests.get(search_endpoint + movie_name)
    items = response.json()["items"]
    video_ids = [each["id"]["videoId"] for each in items]
    return video_ids


def get_video_category_id(video_id):
    '''
    Returns the category_id(an integer) of the video.
    '''

    param = {
        "part": "snippet",
        "id": video_id
    }

    url = f"https://www.googleapis.com/youtube/v3/videos{api_key}"

    response = requests.get(url, params=param)

    data = response.json()

    return int(data["items"][0]["snippet"]["categoryId"])


def get_video_categories_all():
    '''
        Returns a dictionary containing all the categories
    '''
    param = {
        "part": "snippet",
        "regionCode": "NG"
    }

    url = f"https://www.googleapis.com/youtube/v3/videoCategories{api_key}"

    response = requests.get(url, params=param)

    data = response.json()

    categories = {}

    for entry in data["items"]:
        categories[entry["id"]] = entry["snippet"]["title"]

    return categories


def video_category_name_check(category_id_list):
    '''
    Returns the name of the video category
    '''
    category = get_video_categories_all()
    categories = []

    for identity in category_id_list:
        categories.append(category[f'{identity}'])

    return categories


def return_category_from_name(name):
    '''
    Returns the name of the category of the video link
    '''
    videos_ids = get_movies(name)
    categories_ids = [get_video_category_id(video_id) for video_id in videos_ids]
    result = video_category_name_check(categories_ids)

    names = []
    frequency = []
    for name in result:
        if name not in names:
            names.append(name)

    for name in names:
        frequency.append(result.count(name))

    # Creating plot
    # fig = plt.figure(figsize=(7, 5))
    # plt.pie(frequency, labels=names)

    fig = plt.figure(figsize=(5, 3))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    ax.pie(frequency, labels=names, autopct='%1.2f%%')

    # show plot
    plt.show()


