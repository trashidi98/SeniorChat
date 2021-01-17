import React from 'react';
import styled from "styled-components";
import ContactCard from "./ContactCard";
import Sidebar from './Sidebar';
import Header from './Header'


const items = [
  {name: 'home', label:'Home', image: "https://cdn1.iconfinder.com/data/icons/free-98-icons/32/call-512.png"},
  {name: 'searching', label:'Add Friends',image: "https://static.thenounproject.com/png/105498-200.png"},
  {name: 'profile', label: 'Profile',image: "https://icons-for-free.com/iconfiles/png/512/avatar+human+man+profile+icon-1320085876716628234.png"}, 
  {name: 'setting', label: 'Setting',image: "https://simpleicon.com/wp-content/uploads/setting2.png"}, 
]

const CardWrapper = styled.div`
  display: inline-block;
  width: 100%;
  margin-left: 2em;
`;

const AppWrapper = styled.div`
  display: flex;
  flex-direction: column;
`;

const ContentWrapper = styled.div`
  display: flex;
  flex-direction; row;
`

const SidebarPlaceholder = styled.div`
  width: 20em;
  height: 1px;
`

function App(){
  const sayHello = () =>{
    console.log("hello"); 
  }; 
  const counter = 0; 
  console.log(counter);
  return(
    <AppWrapper>
      <Header/>
      <ContentWrapper>
        <CardWrapper>
          <ContactCard name="Family" />
          <ContactCard name="Friends" />
          <ContactCard name="Stephen" />
          <ContactCard name="Sabrina" />
          <ContactCard name="Mom and Dad" />
        </CardWrapper>
        <SidebarPlaceholder/>
        <Sidebar items = {items} />
      </ContentWrapper>
    </AppWrapper>
  );
}
export default App;