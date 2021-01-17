import React from 'react';
import ContactCard from "./ContactCard";
import Sidebar from './Test'
const items = [
  {name: 'home', label:'Home', image: "https://cdn1.iconfinder.com/data/icons/free-98-icons/32/call-512.png"},
  {name: 'searching', label:'Searching',image: "https://static.thenounproject.com/png/105498-200.png"},
  {name: 'profile', label: 'Profile',image: "https://icons-for-free.com/iconfiles/png/512/avatar+human+man+profile+icon-1320085876716628234.png"}, 
  {name: 'setting', label: 'Setting',image: "https://simpleicon.com/wp-content/uploads/setting2.png"}, 
]

function App(){

  const sayHello = () =>{
    console.log("hello"); 
  }; 
  const counter = 0; 
  console.log(counter);
  return(
    <div>
      <ContactCard/>
      <Sidebar items = {items} />
      <h1>Hello React </h1>
      <button> hello </button>
      </div>
  );
}
export default App;
