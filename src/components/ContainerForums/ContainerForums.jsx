import { Fragment } from "react";
import styles from "./ContainerForums.module.css";
import ForumItem from "../ForumItem/ForumItem";
import Card from "../../UI/Card/card"

const ContainerForums = (props) => {
    return(
        <Fragment>
        {!props.isClicked? <div className={styles.column}>
        <Card 
        UIcolor="#D9D9D9" 
        borderRadius="10px">
          <h2>Forums</h2>  
        </Card>
        <Card UIcolor="#D9D9D9" 
        borderRadius="10px">
          <div className={styles.column}>
          {props.list.map((category =>
            <ForumItem 
            key={category.title}
            icon={category.icon} 
            title={category.title} 
            click={() => props.forumHandler(category)}
            />
          ))}
          </div>
        </Card>
        </div> :
        <div className={styles.column}>
        <Card UIcolor="#D9D9D9" 
        borderRadius="10px">
        <div className={styles.row}>
          <h2>{props.title}</h2>  
          <h2 onClick={() => props.createPost}>Create Post</h2>  
        </div>
      </Card>
      <Card UIcolor="#D9D9D9" 
      borderRadius="10px">
        <div className={styles.column}>
        {props.list.map((category =>
          <ForumItem 
          key={category.title}
          icon={category.icon} 
          title={category.title} 
          userName="Posted By User"
          click={() => props.forumHandler(category)}
          />
        ))}
        </div>
      </Card>
      </div> 
        } 
        </Fragment>
    )
}

export default ContainerForums;