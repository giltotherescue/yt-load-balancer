# YouTube Scraper with Load Balancer

A FastAPI service that scrapes YouTube channel metadata and video information.
It uses a load balancer to distribute scraping tasks across multiple cloud services to ensure high availability and
fault tolerance.

## Features

	•	Scrapes channel information (e.g., subscribers, views, description)
	•	Scrapes video details (e.g., titles, views, durations)
	•	Distributes scraping tasks across multiple cloud services using a load balancer
	•	Retries requests in case of failure
	•	Supports API key authentication for secure access
	•	Uses rotating cloud services for scalability and redundancy

___


## Setup

### Local Development

#### 1. Clone this repository:

```bash
  git clone https://github.com/your-username/your-repository.git
```

#### 2. Install Python requirements from requirements.txt:

```bash
  pip install -r requirements.txt
```

#### 3. Copy .env.example to .env and add your API key and other required configurations:

```bash
cp .env.example .env
```

#### 4. Run the FastAPI app:

```bash
  uvicorn main:app --reload
```

The app will start running at http://127.0.0.1:8001.

### Docker Deployment

#### 1. Build the Docker image:

```bash
  docker build -t scraper-load-balancer .
```

#### 2. Run the container:

```bash
    docker run -p 8001:8001 youtube-scraper
```

The service will be available at http://localhost:8001.

___


## API Endpoints

### /scrape

This endpoint scrapes metadata and video information from a YouTube channel.

Method: GET

#### Parameters:

- channelHandle (string): The handle of the YouTube channel to scrape (required).
- maxVideos (integer): The maximum number of videos to scrape. Default is 10.

#### Example Request:

`GET /scrape?channelHandle=@mrbeastl&maxVideos=10`

#### Response:

The service will return a JSON object containing the scraped data:

```
{
    "channel": {
        "banner": {
            "bannerExternalUrl": "https://yt3.googleusercontent.com/5KWiriZZ_KEoEdSMFTJKj2M6vR_XSiRZeQ-ix0cvG3TGZuGoi8sfAjrSiZAP0GzXBkmF8ZGytw"
        },
        "channel_id": "UCX6OQ3DkcsbYNE6H8uQQuVA",
        "country": "United States",
        "custom_url": "@MrBeast",
        "default_language": null,
        "description": "Go Watch Beast Games! https://unfur.ly/BeastGames\nSUBSCRIBE FOR A COOKIE!\n\nAccomplishments:\n- Raised $20,000,000 To Plant 20,000,000 Trees\n- Removed 30,000,000 pounds of trash from the ocean\n- Helped 2,000 people walk again\n- Helped 1,000 blind people see\n- Helped 1,000 deaf people hear\n- Built wells in Africa\n- Built and gave away 100 houses\n- Adopted every dog in a shelter (twice)\n- Given millions to charity\n- Started my own snack company Feastables\n- Started my own software company Viewstats\n- Started Lunchly, a tasty, better-for-you lunch option\n- Gave away a private island (twice)\n- Gave away 1 million meals\n- Gave away a chocolate factory\n- I counted to 100k\n- Ran a marathon in the world's largest shoes\n- Survived 50 hours in Antarctica\n- Recreated Squid Game in real life\n- Created the largest competition show with 1000 people (Beast Games)\n- Gave $5,000,000 to one person\n- Passed T-Series to become most subscribed YouTube channel 🥹\nyou get it, I appreciate all of you so much :)\n",
        "keywords": [
            "mrbeast6000 beast mrbeast Mr.Beast mr"
        ],
        "made_for_kids": false,
        "published_at": "2012-02-20 00:00:00",
        "subscriber_count": 367000000,
        "thumbnails": {
            "default": {
                "height": 900,
                "url": "https://yt3.googleusercontent.com/nxYrc_1_2f77DoBadyxMTmv7ZpRZapHR5jbuYe7PlPd5cIRJxtNNEYyOC0ZsxaDyJJzXrnJiuDE=s900-c-k-c0x00ffffff-no-rj",
                "width": 900
            },
            "high": {
                "height": 900,
                "url": "https://yt3.googleusercontent.com/nxYrc_1_2f77DoBadyxMTmv7ZpRZapHR5jbuYe7PlPd5cIRJxtNNEYyOC0ZsxaDyJJzXrnJiuDE=s900-c-k-c0x00ffffff-no-rj",
                "width": 900
            },
            "medium": {
                "height": 900,
                "url": "https://yt3.googleusercontent.com/nxYrc_1_2f77DoBadyxMTmv7ZpRZapHR5jbuYe7PlPd5cIRJxtNNEYyOC0ZsxaDyJJzXrnJiuDE=s900-c-k-c0x00ffffff-no-rj",
                "width": 900
            }
        },
        "title": "MrBeast",
        "video_count": 849,
        "view_count": 73941646670
    },
    "metadata": {
        "failed_videos_details": null,
        "total_videos_found": 10,
        "videos_failed": 0,
        "videos_processed": 10
    },
    "videos": [
        {
            "duration": "PT21M43S",
            "published_at": "2025-02-13 09:50:34",
            "thumbnails": {
                "default": {
                    "height": 90,
                    "url": "https://i.ytimg.com/vi/NDsO1LT_0lw/default.jpg",
                    "width": 120
                },
                "high": {
                    "height": 360,
                    "url": "https://i.ytimg.com/vi/NDsO1LT_0lw/hqdefault.jpg",
                    "width": 480
                },
                "medium": {
                    "height": 180,
                    "url": "https://i.ytimg.com/vi/NDsO1LT_0lw/mqdefault.jpg",
                    "width": 320
                }
            },
            "title": "I Spent 100 Hours Inside The Pyramids!",
            "url": "https://www.youtube.com/watch?v=NDsO1LT_0lw",
            "video_id": "NDsO1LT_0lw",
            "view_count": 141000000
        },
        {
            "duration": "PT34M46S",
            "published_at": "2025-01-28 09:50:34",
            "thumbnails": {
                "default": {
                    "height": 90,
                    "url": "https://i.ytimg.com/vi/sF5LYGgKbUA/default.jpg",
                    "width": 120
                },
                "high": {
                    "height": 360,
                    "url": "https://i.ytimg.com/vi/sF5LYGgKbUA/hqdefault.jpg",
                    "width": 480
                },
                "medium": {
                    "height": 180,
                    "url": "https://i.ytimg.com/vi/sF5LYGgKbUA/mqdefault.jpg",
                    "width": 320
                }
            },
            "title": "Every Minute One Person Is Eliminated",
            "url": "https://www.youtube.com/watch?v=sF5LYGgKbUA",
            "video_id": "sF5LYGgKbUA",
            "view_count": 92000000
        },
        {
            "duration": "PT15M31S",
            "published_at": "2025-01-28 09:50:34",
            "thumbnails": {
                "default": {
                    "height": 90,
                    "url": "https://i.ytimg.com/vi/SM66GDRyIVY/default.jpg",
                    "width": 120
                },
                "high": {
                    "height": 360,
                    "url": "https://i.ytimg.com/vi/SM66GDRyIVY/hqdefault.jpg",
                    "width": 480
                },
                "medium": {
                    "height": 180,
                    "url": "https://i.ytimg.com/vi/SM66GDRyIVY/mqdefault.jpg",
                    "width": 320
                }
            },
            "title": "I Helped 2,000 People Walk Again",
            "url": "https://www.youtube.com/watch?v=SM66GDRyIVY",
            "video_id": "SM66GDRyIVY",
            "view_count": 90000000
        },
        {
            "duration": "PT24M45S",
            "published_at": "2024-12-29 09:50:34",
            "thumbnails": {
                "default": {
                    "height": 90,
                    "url": "https://i.ytimg.com/vi/gs8qfL9PNac/default.jpg",
                    "width": 120
                },
                "high": {
                    "height": 360,
                    "url": "https://i.ytimg.com/vi/gs8qfL9PNac/hqdefault.jpg",
                    "width": 480
                },
                "medium": {
                    "height": 180,
                    "url": "https://i.ytimg.com/vi/gs8qfL9PNac/mqdefault.jpg",
                    "width": 320
                }
            },
            "title": "2,000 People Fight For $5,000,000",
            "url": "https://www.youtube.com/watch?v=gs8qfL9PNac",
            "video_id": "gs8qfL9PNac",
            "view_count": 160000000
        },
        {
            "duration": "PT22M45S",
            "published_at": "2024-12-29 09:50:34",
            "thumbnails": {
                "default": {
                    "height": 90,
                    "url": "https://i.ytimg.com/vi/0BjlBnfHcHM/default.jpg",
                    "width": 120
                },
                "high": {
                    "height": 360,
                    "url": "https://i.ytimg.com/vi/0BjlBnfHcHM/hqdefault.jpg",
                    "width": 480
                },
                "medium": {
                    "height": 180,
                    "url": "https://i.ytimg.com/vi/0BjlBnfHcHM/mqdefault.jpg",
                    "width": 320
                }
            },
            "title": "Beat Ronaldo, Win $1,000,000",
            "url": "https://www.youtube.com/watch?v=0BjlBnfHcHM",
            "video_id": "0BjlBnfHcHM",
            "view_count": 223000000
        },
        {
            "duration": "PT17M40S",
            "published_at": "2024-11-29 09:50:34",
            "thumbnails": {
                "default": {
                    "height": 90,
                    "url": "https://i.ytimg.com/vi/Xj0Jtjg3lHQ/default.jpg",
                    "width": 120
                },
                "high": {
                    "height": 360,
                    "url": "https://i.ytimg.com/vi/Xj0Jtjg3lHQ/hqdefault.jpg",
                    "width": 480
                },
                "medium": {
                    "height": 180,
                    "url": "https://i.ytimg.com/vi/Xj0Jtjg3lHQ/mqdefault.jpg",
                    "width": 320
                }
            },
            "title": "$1 vs $500,000 Experiences!",
            "url": "https://www.youtube.com/watch?v=Xj0Jtjg3lHQ",
            "video_id": "Xj0Jtjg3lHQ",
            "view_count": 199000000
        },
        {
            "duration": "PT20M35S",
            "published_at": "2024-10-30 09:50:34",
            "thumbnails": {
                "default": {
                    "height": 90,
                    "url": "https://i.ytimg.com/vi/bn0Kh9c4Zv4/default.jpg",
                    "width": 120
                },
                "high": {
                    "height": 360,
                    "url": "https://i.ytimg.com/vi/bn0Kh9c4Zv4/hqdefault.jpg",
                    "width": 480
                },
                "medium": {
                    "height": 180,
                    "url": "https://i.ytimg.com/vi/bn0Kh9c4Zv4/mqdefault.jpg",
                    "width": 320
                }
            },
            "title": "7 Days Exploring An Underground City",
            "url": "https://www.youtube.com/watch?v=bn0Kh9c4Zv4",
            "video_id": "bn0Kh9c4Zv4",
            "view_count": 131000000
        },
        {
            "duration": "PT35M40S",
            "published_at": "2024-10-30 09:50:34",
            "thumbnails": {
                "default": {
                    "height": 90,
                    "url": "https://i.ytimg.com/vi/snX5YyflrGw/default.jpg",
                    "width": 120
                },
                "high": {
                    "height": 360,
                    "url": "https://i.ytimg.com/vi/snX5YyflrGw/hqdefault.jpg",
                    "width": 480
                },
                "medium": {
                    "height": 180,
                    "url": "https://i.ytimg.com/vi/snX5YyflrGw/mqdefault.jpg",
                    "width": 320
                }
            },
            "title": "100 Identical Twins Fight For $250,000",
            "url": "https://www.youtube.com/watch?v=snX5YyflrGw",
            "video_id": "snX5YyflrGw",
            "view_count": 138000000
        },
        {
            "duration": "PT31M48S",
            "published_at": "2024-09-30 09:50:34",
            "thumbnails": {
                "default": {
                    "height": 90,
                    "url": "https://i.ytimg.com/vi/aRcUVhVlSHg/default.jpg",
                    "width": 120
                },
                "high": {
                    "height": 360,
                    "url": "https://i.ytimg.com/vi/aRcUVhVlSHg/hqdefault.jpg",
                    "width": 480
                },
                "medium": {
                    "height": 180,
                    "url": "https://i.ytimg.com/vi/aRcUVhVlSHg/mqdefault.jpg",
                    "width": 320
                }
            },
            "title": "Men Vs Women Survive The Wilderness For $500,000",
            "url": "https://www.youtube.com/watch?v=aRcUVhVlSHg",
            "video_id": "aRcUVhVlSHg",
            "view_count": 155000000
        },
        {
            "duration": "PT17M59S",
            "published_at": "2024-08-31 09:50:34",
            "thumbnails": {
                "default": {
                    "height": 90,
                    "url": "https://i.ytimg.com/vi/ndAQfTzlVjc/default.jpg",
                    "width": 120
                },
                "high": {
                    "height": 360,
                    "url": "https://i.ytimg.com/vi/ndAQfTzlVjc/hqdefault.jpg",
                    "width": 480
                },
                "medium": {
                    "height": 180,
                    "url": "https://i.ytimg.com/vi/ndAQfTzlVjc/mqdefault.jpg",
                    "width": 320
                }
            },
            "title": "7 Days Stranded In A Cave",
            "url": "https://www.youtube.com/watch?v=ndAQfTzlVjc",
            "video_id": "ndAQfTzlVjc",
            "view_count": 141000000
        }
    ]
}
```

#### Errors:
- 500 Internal Server Error: If the maximum retry attempts are exceeded.
- 400 Bad Request: If the request parameters are invalid.

___

## Service Architecture

### Load Balancer

The service uses a load balancer to distribute requests across multiple cloud services. It randomly selects one service
from a list of available services in different regions, excluding the previously used service. This ensures that the
scraping process is distributed evenly, improving performance and fault tolerance.

### Authentication

API key authentication is required to use the service. The API key can be passed as X-API-Key header.
For requests to cloud services, ID tokens are generated to authenticate against Google Cloud.

### Request Retry

If a request to a cloud service fails, the service will automatically retry up to a configured number of attempts. This
ensures that transient issues do not cause the scraping process to fail entirely.

### Cloud Services Integration

The service interacts with multiple cloud services deployed across different Google Cloud regions. The list of available
services is dynamically fetched from Google Cloud Run using the get_all_cloud_run_service_uris function.

### Configuration

The application settings can be configured in the app/settings directory. Key configurations include:
- API_KEY: The API key used for authentication.
- MAX_RETRIES: The maximum number of retry attempts for failed requests.

Make sure to update the environment variables in the .env file for local development or cloud deployment.

___

## Conclusion

This service provides a robust and scalable solution for scraping YouTube data. With the load balancer, retry logic, and
integration with cloud services, it ensures that scraping tasks are efficiently distributed, providing high availability
and fault tolerance.

___

# Deploy to GCP

### Install Google Cloud CLI
[https://cloud.google.com/sdk/docs/install](Install Google Cloud CLI)

### Authenticate with Google Cloud
```bash
  gcloud auth login
```
Follow the instructions in the browser to authenticate.

### Set the project
```bash
  gcloud config set project <PROJECT_ID>
```

### Set correct environment variables in .env

- SERVER_PORT=8001 -> Port from the Dockerfile
- PROJECT_ID=your-project-id-here -> Google Cloud project ID
- GLOBAL_NAME_PREFIX=ps -> Global prefix for all resources
- SUB_NAME_PREFIX=load-balancer -> Service name prefix
- ARTIFACT_REPO=${GLOBAL_NAME_PREFIX}-repo -> Artifact repository name
- REPO_REGION=us -> Artifact repository region
- REGION=us-east1 -> Region where the service will be deployed (only one region)


### Build and push Docker image to Google Cloud then deploy to Google Cloud Run
This will build the Docker image, tag it with the Google Cloud registry URL, and push it to the registry then deploy the service to Google Cloud Run.
```bash
  sh deploy_scripts/deploy-to-cr.sh
```
