import React from 'react';
import List from '@material-ui/core/List'
import ListItem from '@material-ui/core/ListItem'
import ListItemText from '@material-ui/core/ListItemText'
const styles = theme => ({
  listItemText:{
    fontSize:'1.7em',//Insert your required size
  }
});
function Sidebar({ items }) {
  return (
    <div className = "sidebar">
    <List disablePadding dense>
      {items.map(({ label, name,image, ...rest }) => (
        <ListItem key={name} button {...rest}> 
        <img src = {image} width="40" height="40"></img>
          <ListItemText>{label}</ListItemText>
          
        </ListItem>
      ))}
    </List>


    </div>
  )
}

export default Sidebar
