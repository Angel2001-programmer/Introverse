import styles from "./button.module.css"

const Button = props => {
    return(
        <button className={styles.button} type={props.type} onClick={props.click} 
        style={{
            background: props.UIcolor, 
            borderColor: props.borderColor, 
            boxShadow: props.dropShadow,
            paddingLeft: props.paddingToLeft,
            paddingRight: props.paddingToRight,
        }}>
            <p>{props.text}</p>
        </button>
    )
}

export default Button; 