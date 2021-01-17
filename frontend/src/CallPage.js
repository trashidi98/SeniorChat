import React from 'react';
import styled from "styled-components";


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
  padding-bottom: 1em;
`

const CallWindow = styled.div`
  background-color: #dbdbdb;
  width: 70em;
  height: 50em;
`

function CallPage(props){
  return(
    <CallWrapper>
      <CallTitle>Calling {props.callGroup}</CallTitle>
      <CallWindow/>
    </CallWrapper>
  );
}
export default CallPage;
