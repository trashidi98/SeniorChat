import React, { useState } from 'react';
import styled from "styled-components";
import Home from './HomePage'
import CallPage from './CallPage'
import Sidebar from './Sidebar';
import Header from './Header'
import Signin from './Signin'

const items = [
  {name: 'home', pageLink: "home", label:'Home', image: "https://cdn1.iconfinder.com/data/icons/free-98-icons/32/call-512.png"},
  {name: 'searching', pageLink: "addFriends", label:'Add Friends',image: "https://static.thenounproject.com/png/105498-200.png"},
  {name: 'profile', pageLink: "profile", label: 'Profile',image: "https://icons-for-free.com/iconfiles/png/512/avatar+human+man+profile+icon-1320085876716628234.png"}, 
  {name: 'settings', pageLink: "settings", label: 'Settings',image: "https://simpleicon.com/wp-content/uploads/setting2.png"}, 
]

const AppWrapper = styled.div`
  display: flex;
  flex-direction: column;
`;

const ContentWrapper = styled.div`
  display: flex;
  flex-direction; row;
  justify-content: center;
  align-items: center;
`

const SidebarPlaceholder = styled.div`
  width: 20em;
  height: 1px;
`

const router = (currentPage, setCurrentPage, callGroup, setCallGroup) => {
  if (currentPage == "home") {
    return <Home setCurrent={() => {setCurrentPage("call")}} setGroup={setCallGroup} />;
  }
  else if (currentPage == "call") {
    return <CallPage callGroup={callGroup} />;
  }
}

function App(){
  const [currentPage, setCurrentPage] = useState("signin");
  const [callGroup, setCallGroup] = useState("N/A");

  if (currentPage == "signin") {
    return <Signin/>
  }

  return(
    <AppWrapper>
      <Header/>
      <ContentWrapper>
        {router(currentPage, setCurrentPage, callGroup, setCallGroup)}
        <SidebarPlaceholder/>
        <Sidebar items = {items} setCurrent={setCurrentPage}/>
      </ContentWrapper>
    </AppWrapper>
  );
}
export default App;
