import React from 'react';
import styled from "styled-components";
import img from "./images/family.jpg"

const ContactCardBackground = styled.div`
  background-image: url(${img});
  font-size: 32px;
  color: white;
`;

function ContactCard(){

  return(
    <ContactCardBackground>
      <div>
        <p>Family</p>
      </div>
    </ContactCardBackground>
  );
}
export default ContactCard;
