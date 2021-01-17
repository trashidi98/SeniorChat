import React from 'react';
import List from '@material-ui/core/List'
import styled from "styled-components";


const SidebarWrapper = styled.div`
  border-left: 1px solid rgba(0,0,0);
  width: 20em;
  position: fixed;
  right: 0px;
  top: 0px;
  height: 100%;
`;

const SidebarItem = styled.div`
  font-size: 1.7em;
  padding: 0.5em;
  margin: 0em;
  display: flex;
  flex-direction: row;
  align-items: center;
  &:hover {
    background-color: #eaf24e;
  }
`;

const HeaderItem = styled.div`
  font-size: 2em;
  padding: .7em;
  padding-bottom: 1em;
  margin: 0em;
  display: flex;
  flex-direction: row;
  align-items: center;
  font-weight: bold;
`;

const SidebarLabel = styled.div`
  padding-left: 0.2em;
`;

function Sidebar({ items, setCurrent }) {
  return (
    <SidebarWrapper>
      <List disablePadding dense>
        <HeaderItem>SeniorChat</HeaderItem>
        {items.map(({ label, name, image, pageLink, ...rest }) => (
          <SidebarItem key={name} button {...rest} onClick={() => {setCurrent(pageLink)}} > 
          <img src = {image} width="40" height="40"></img>
          <SidebarLabel>{label}</SidebarLabel>  
          </SidebarItem>
        ))}
      </List>
    </SidebarWrapper>
  )
}

export default Sidebar
