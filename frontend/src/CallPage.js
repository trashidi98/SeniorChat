import React from 'react';
import styled from "styled-components";
import { connect, createLocalVideoTrack } from "twilio-video";

const TEST_TOKEN = "hidden"

const CallWrapper = styled.div`
  padding: 2em;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
`;

const CallTitle = styled.div`
  font-size: 2.5em;
  font-weight: bold;
`

const CallInnerWrapper = styled.div`
  background-color: #fafafa;
  width: 80em;
  margin: 3em;
`

const CallWindow = styled.div`
  display: inline-block;
`

const watchSelf = () => {
  createLocalVideoTrack().then(track => {
    const localMediaContainer = document.getElementById('local-media');
    localMediaContainer.appendChild(track.attach());
  });
}

const joinRoom = (roomName) => {
  connect(TEST_TOKEN, { audio: true, name: roomName, video: { width: 640 } }).then(room => {
    console.log(`Successfully joined a Room: ${room}`);

    // Get video for already connected participants
    room.participants.forEach(participant => {
      participant.tracks.forEach(publication => {
        if (publication.track) {
          document.getElementById('remote-media-div').appendChild(publication.track.attach());
        }
      });
    
     participant.on('trackSubscribed', track => {
        document.getElementById('remote-media-div').appendChild(track.attach());
      });
    });


    room.on('participantConnected', participant => {
      console.log(`A remote Participant connected: ${participant}`);

      // Get video for newly connected participants
      participant.tracks.forEach(publication => {
        if (publication.isSubscribed) {
          const track = publication.track;
          document.getElementById('remote-media-div').appendChild(track.attach());
        }
      });
    
      participant.on('trackSubscribed', track => {
        document.getElementById('remote-media-div').appendChild(track.attach());
      });

    });
  }, error => {
    console.error(`Unable to connect to Room: ${error.message}`);
  });
};

function CallPage(props){
  watchSelf();
  joinRoom("what");
  return(
    <CallWrapper>
      <CallTitle>Calling {props.callGroup}</CallTitle>
      <CallInnerWrapper>
        <CallWindow id="local-media" />
        <CallWindow id="remote-media-div" height="50em" />
      </CallInnerWrapper>
    </CallWrapper>
  );
}
export default CallPage;
