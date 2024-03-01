import os
from fastapi import FastAPI
from livepeer_client import LivepeerText2VideoClient
import sc_utils as sc


app = FastAPI()
livepeer = LivepeerText2VideoClient(api_key=os.environ["LIVEPEER_API_KEY"])


@app.post("/generate-video")
async def generate_video(prompt: str, video_name: str):
    # Generate the video using the prompt and video name
    livepeer.generate_and_upload_video(prompt, video_name)
    return {"message": "Video generated and uploaded successfully"}


@app.post("/vote")
async def vote(video_uuid: str, from_address: str):
    # Call the vote function of the contract
    sc.vote(video_uuid, from_address)
    return {"message": "Vote cast successfully"}


@app.get("/get-votes")
async def get_votes(video_uuid: str) -> int:
    # Call the getVotes function of the contract
    num_vote = sc.get_votes(video_uuid)
    return num_vote


# define the main function
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
