import requests


class LivepeerText2VideoClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = " https://livepeer.studio/api"
        self.text2video_url = "http://209.20.157.253:8000"

    def _upload_video(self, video_name: str, video_url: str) -> None:
        header = {"Authorization": f"Bearer {self.api_key}"}
        resp = requests.post(
            f"{self.base_url}/asset/upload/url",
            headers=header,
            json={
                "name": video_name,
                "url": video_url,
            },
        )
        print("Video Uploading Result")
        print(resp.json())

    def generate_video(self, prompt: str) -> str:
        """Send a generation request to FLock's text2video model and get a signed
        S3 URL to upload the video to.

        Args:
            prompt (str): The prompt to generate the video from
        """
        resp = requests.post(f"{self.text2video_url}/generate", json={"prompt": prompt})
        return resp.json()["signed_s3_url"]

    def generate_and_upload_video(self, prompt: str, video_name: str) -> None:
        """Generate a video from a prompt and upload it to Livepeer.

        Args:
            prompt (str): The prompt to generate the video from
            video_name (str): The name to give the video
        """
        video_url = self.generate_video(prompt)
        self._upload_video(video_name, video_url)
