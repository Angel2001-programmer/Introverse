import styles from "./userInput.module.css"
import { useContext, useState } from 'react'
import { UserContext } from "../../components/FinalProject/FinalProject";;

const UserInput = props => {
    const [isOpened, setIsOpened]  = useContext(UserContext);
    let closeModal = null

    if(props.title !== ""){
        closeModal= 
            <div className= {styles.rowTop}>
            <h2 className={styles.closeModal} onClick={props.isClose}>{props.isCloseIcon}</h2>
            <h2 className={styles.title}>{props.title}</h2>
            </div>
    } else {
        closeModal = 
            <div className= {styles.rowTop}>
            <h2 className={styles.title}>{props.title}</h2>
            </div>
    }
    return(
        <div>
            {closeModal}
            <label className={styles.userLabel} 
            htmlFor={props.for}
            >{props.labelName}</label>
            
            <input className={styles.userField} 
            type={props.type} 
            value={props.value} 
            name={props.name} 
            onChange={props.onValue}
            maxLength={props.length}
            placeholder={props.placeholder}/>
        </div>
    )
}

export default UserInput;