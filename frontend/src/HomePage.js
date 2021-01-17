import React, { useState } from 'react';
import styled from "styled-components";
import ContactCard from './ContactCard';

const CardWrapper = styled.div`
  display: inline-block;
  width: 100%;
  margin-left: 2em;
`;

function Home(props){
  return(
    <CardWrapper>
      <ContactCard name="Family" setCurrent={props.setCurrent} setGroup={props.setGroup} />
      <ContactCard name="Friends" setCurrent={props.setCurrent} setGroup={props.setGroup}/>
      <ContactCard name="Stephen" setCurrent={props.setCurrent} setGroup={props.setGroup}/>
      <ContactCard name="Sabrina" setCurrent={props.setCurrent} setGroup={props.setGroup}/>
      <ContactCard name="Mom and Dad" setCurrent={props.setCurrent} setGroup={props.setGroup} />
    </CardWrapper>
  );
}
export default Home;
