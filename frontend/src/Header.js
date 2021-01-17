import React from 'react';
import styled from "styled-components";

const SearchBar = styled.input`
  font-size: 2em;
  width: 15em;
  margin: 0.75em;
  border: 0.05em solid #575757;
  padding: 0.1em;
  padding-left: 0.3em;
  border-radius: 0.3em;
`;

const SearchIcon = styled.img`
  height: 3em;
  width: 3em;
  padding-left: 2em;
`

const SearchWrapper = styled.div`
  display: flex;
  align-items: center;
`;

function Header() {
  return (
    <SearchWrapper>
      <SearchIcon src="https://static.thenounproject.com/png/105498-200.png" />
      <SearchBar placeholder="Search Contacts" />
    </SearchWrapper>
  )
}

export default Header
