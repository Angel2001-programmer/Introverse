import styles from './listItem.module.css'

const ListItem = props => {
    return(
    <div className={styles.card}>
        <img src={props.image} alt="Placeholder."/>
        <p>{props.name}</p>
        <p>{props.description}</p>
    </div>
    )
}
export default ListItem;