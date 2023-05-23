import React from 'react';
import { Typography, Container } from '@mui/material';
import { styled } from '@mui/system';

const FooterContainer = styled('footer')(({ theme }) => ({
  backgroundColor: theme.palette.primary.main,
  color: theme.palette.primary.contrastText,
  padding: theme.spacing(2),
}));

const Footer = () => {
  return (
    <FooterContainer>
      <Container maxWidth="sm">
        <Typography variant="body2" align="center">
          Footer content
        </Typography>
      </Container>
    </FooterContainer>
  );
};

export default Footer;