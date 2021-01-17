import React from 'react';
import styled from "styled-components";
import img from "./images/family.jpg"

const ContactCardBackground = styled.div`
  background-image: url(${img});
  background-size: cover;
  height: 20em;
  width: 30em;
  border-radius: 1.5em;
`;

const ContactCardTextShadow = styled.div`
  background-color: rgba(0, 0, 0, 0.2);
`;

const ContactCardText = styled.p`
  font-size: 2em;
  opacity: 1.0;
  padding: 0.4em;
  text-align: center;
  font-weight: bold;
`;

function ContactCard(){
  return(
    <ContactCardBackground>
      <ContactCardTextShadow>
        <ContactCardText>Family</ContactCardText>
      </ContactCardTextShadow>
    </ContactCardBackground>
  );
}
export default ContactCard;
