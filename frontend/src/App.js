import React from 'react';
import styled from "styled-components";
import ContactCard from "./ContactCard";
import Sidebar from './Test'
const items = [
  {name: 'home', label:'Home'},
  {name: 'searching', label:'Searching'},
  {name: 'profile', label: 'Profile'}, 
  {name: 'setting', label: 'Setting'}, 
]

const CardWrapper = styled.div`
  display: inline-block;
  width: 100%;
  margin-left: 2em;
`;

function App(){

  const sayHello = () =>{
    console.log("hello"); 
  }; 
  const counter = 0; 
  console.log(counter);
  return(
    <div>
      <Sidebar items = {items} />
      <CardWrapper>
        <ContactCard name="Family" />
        <ContactCard name="Friends" />
        <ContactCard name="Stephen" />
        <ContactCard name="Sabrina" />
        <ContactCard name="Mom and Dad" />
      </CardWrapper>
    </div>
  );
}
export default App;
