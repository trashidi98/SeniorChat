import React, { useState } from 'react';
import styled from "styled-components";
import ContactCard from './ContactCard';
import familyImage from "./images/family.jpg"
import friendsImage from "./images/friends.jpg"
import stephenImage from "./images/stephen.png"
import sabrinaImage from "./images/sabrina.png"

const CardWrapper = styled.div`
  display: inline-block;
  width: 100%;
  margin-left: 2em;
`;

function Home(props){
  return(
    <CardWrapper>
      <ContactCard name="Family" image={familyImage} setCurrent={props.setCurrent} setGroup={props.setGroup} />
      <ContactCard name="Friends" image={friendsImage} setCurrent={props.setCurrent} setGroup={props.setGroup}/>
      <ContactCard name="Stephen" image={stephenImage} setCurrent={props.setCurrent} setGroup={props.setGroup}/>
      <ContactCard name="Sabrina" image={sabrinaImage} setCurrent={props.setCurrent} setGroup={props.setGroup}/>
    </CardWrapper>
  );
}
export default Home;
