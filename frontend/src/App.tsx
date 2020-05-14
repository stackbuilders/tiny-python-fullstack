import React from "react";
import { Card, Form } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <div className="App-header">
        <Card style={{ width: "18rem" }}>
          <Card.Header>
            <Form>
              <Form.Group controlId="formBasicEmail">
                <Form.Control type="text" placeholder="Type username + enter" />
              </Form.Group>
            </Form>
          </Card.Header>
          <Card.Img variant="top" src={logo} />
          <Card.Body>
            <Card.Title>Github User</Card.Title>
            <Card.Subtitle>Location</Card.Subtitle>
          </Card.Body>
          <Card.Footer>
            <Card.Text>147 Followers</Card.Text>
            <Card.Text>33 Repositories</Card.Text>
            <Card.Text>5 Following</Card.Text>
          </Card.Footer>
        </Card>
      </div>
    </div>
  );
}

export default App;
