import React from 'react';
import styled from "styled-components";
import img from "./images/family.jpg"

const ContactCardTextShadow = styled.div`
  background-color: rgba(255, 255, 255, 0.4);
  width: 100%;
  height: 50%;
  transition: transform .3s ease-out;
  transform: translate(0, 50%);
  display: flex;
  align-items: flex-begin;
  justify-content: center;
`;

const ContactCardText = styled.p`
  font-size: 2em;
  opacity: 1.0;
  margin: 0em;
  font-weight: bold;
  transition: transform .3s ease-out;
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
    transform: translate(0, 0);
  }
`;

const ContactCardWrapper = styled.div`
  display: inline-block;
  margin-right: 5em;
  margin-bottom: 5em;
`

function ContactCard(props){
  return(
    <ContactCardWrapper onClick={() => {props.setGroup(props.name); props.setCurrent()}}>
      <ContactCardBackground>
        <ContactCardTextShadow>
          <ContactCardText>{props.name}</ContactCardText>
        </ContactCardTextShadow>
      </ContactCardBackground>
    </ContactCardWrapper>
  );
}
export default ContactCard;
