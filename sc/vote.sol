// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VideoVoting {
    // Stores the number of votes for each video, using the video's UUID as a unique identifier
    mapping(string => uint256) public votes;

    // Records whether each user has voted for each video to prevent duplicate voting
    // Mapping format: user address => (video UUID => has voted)
    mapping(address => mapping(string => bool)) public hasVoted;

    // Event triggered when a vote occurs
    event Voted(address indexed voter, string videoUUID);

    // Voting function
    function vote(string memory videoUUID) public {
        require(!hasVoted[msg.sender][videoUUID], "You have already voted for this video.");
        
        votes[videoUUID]++;
        hasVoted[msg.sender][videoUUID] = true;
        
        emit Voted(msg.sender, videoUUID);
    }

    // Get the total number of votes for a specific video
    function getVotes(string memory videoUUID) public view returns (uint256) {
        return votes[videoUUID];
    }
}