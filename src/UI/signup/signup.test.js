import {render, screen, fireEvent} from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import '@testing-library/jest-dom'
import SignUp from './signup'
import Button from "../Button/button"
// Tried importing everything but still gives errors
import styles from "./signup.module.css";
import UserInput from "../UserInput/userInput"
import Card from "../Card/card";
import { useState, useContext } from "react";
import { SignUpContext, UserContext, NewUserContext } from "../../components/FinalProject/FinalProject";
import httpClient from "../../httpClient";
import { login } from "../../auth";

describe("SignUp", () => {
  // Test component loading
  test("Loads up and displays a button component", () => {
    // Arrange
    render(<Button />)

    // Act
    // const buttonTitle = screen.getByLabelText("submitBtn")
    const submitButton = screen.getAllByRole("button")

    // Assert
    expect(submitButton).toHaveTextContent("Create an account")

  })
})