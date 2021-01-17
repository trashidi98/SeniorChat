import React from 'react';
import styled from "styled-components";
import img from "./images/family.jpg"

const ContactCardTextShadow = styled.div`
  background-color: rgba(255, 255, 255, 0.4);
  width: 100%;
`;

const ContactCardText = styled.p`
  font-size: 2em;
  opacity: 1.0;
  padding: 0.5em;
  margin: 0em;
  text-align: center;
  font-weight: bold;
`;

const ContactCardBackground = styled.div`
  background-image: url(${img});
  background-size: cover;
  height: 20em;
  width: 30em;
  border-radius: 1.5em;
  border : 0.4em solid black;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  &:hover ${ContactCardTextShadow} {
    background-color: rgba(181, 178, 25, 0.4);
  }
`;

const ContactCardWrapper = styled.div`
  display: inline-block;
  margin-right: 5em;
  margin-bottom: 5em;
`

function ContactCard(props){
  return(
    <ContactCardWrapper>
      <ContactCardBackground>
        <ContactCardTextShadow>
          <ContactCardText>{props.name}</ContactCardText>
        </ContactCardTextShadow>
      </ContactCardBackground>
    </ContactCardWrapper>
  );
}
export default ContactCard;
