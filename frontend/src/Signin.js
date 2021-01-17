import React from 'react';
import styled from "styled-components";

const SigninWrapper = styled.div`
  padding: 2em;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
`;

function Signin() {
  return (
    <SigninWrapper>
      Signin page here
    </SigninWrapper>
  )
}

export default Signin
