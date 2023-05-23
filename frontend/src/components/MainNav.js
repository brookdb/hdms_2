import React from 'react';
import { Link } from 'react-router-dom';
import { Box, AppBar, Toolbar, Typography } from '@mui/material';
import { styled } from '@mui/system';

const NavLink = styled(Link)(({ theme }) => ({
  color: theme.palette.common.white,
  textDecoration: 'none',
  marginRight: theme.spacing(2),
  '&:hover': {
    textDecoration: 'underline',
  },
}));

const MainNav = () => {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          <NavLink to="/">Merrit Hospital</NavLink>
        </Typography>
        <Box>
          <NavLink to="/about">About</NavLink>
          <NavLink to="/contact">Contact</NavLink>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default MainNav;
