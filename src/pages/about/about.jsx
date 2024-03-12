import { Fragment, useState } from 'react';
import styles from './about.module.css';
import Angel from '../../assets/img/TeamMembers/angel.jpg';
import Katherine from '../../assets/img/TeamMembers/katherine.png';
import Katalin from '../../assets/img/TeamMembers/katalin.png';
import Abbie from '../../assets/img/TeamMembers/abbie.jpg';
import TeamMemeber from '../../components/TeamMember/teamMember';
import NavBar from '../../components/NavBar/navbar';
import DropDownMenu from '../../components/DropDownMenu/dropDownMenu';
import Charities from '../../components/Charities/Charities';

export default function About() {
  const [isPressed, setIsPressed] = useState(false);

  return (
    <Fragment>
      <NavBar
        isPressed={isPressed}
        onChangePressed={setIsPressed}
      />
      <DropDownMenu
        isPressed={isPressed}
        setIsPressed={setIsPressed}
      />
      <main className='main'>
        <section className={styles.content}>
          <p className='mainText'>About</p>
          <h2 className='missionTitle'>Our Mission</h2>
          <p className='missionText'>
            At Introverse, we are dedicated to nurturing the mental well-being
            of introverts who cherish the worlds of anime, gaming and
            literature. We understand that finding a community where you can
            truly belong and express your passions can be a transformative
            experience. Our mission is to create an inviting digital haven where
            introverts can connect, share, and engage in meaningful
            conversations about anime, games and reading. We strive to offer a
            platform that resonates with the unique needs and preferences of our
            audience, providing a space that feels like home. Here, every voice
            is valued, every interest is celebrated, and every individual is
            encouraged to embrace their love for anime, literature and gaming.
            Our commitment extends beyond creating a community; it's about
            fostering an environment where introverts can flourish, find
            like-minded friends, and feel empowered to explore their passions
            without any reservations. In this journey, we are not just building
            a website; we are crafting a sanctuary where the beauty of solitude
            meets the warmth of togetherness, all centred around the shared love
            for anime, games and books.
          </p>
          <p className='mainText2'>The Team!</p>
          <div className={styles.about}>
            <TeamMemeber
              name='Angel'
              profilepictrue={Angel}
              hobby='Coding websites in my spare time.'
              description='To get a job and have a good life'
            />

            <TeamMemeber
              name='Katalin'
              profilepictrue={Katalin}
              hobby='Weight lifting and gaming.'
              description='To be strong and have a quick trigger finger.'
            />

            <TeamMemeber
              name='Abbie'
              profilepictrue={Abbie}
              hobby='Reading'
              description='For mental stimulation and relaxation'
            />

            <TeamMemeber
              name='Katherine Hooper'
              profilepictrue={Katherine}
              hobby='I enjoy running and kickboxing'
              description='Running feels freeing and helps me think. Kickboxing makes me feel connected and in control. I love to challenge myself and work hard to progress and improve.'
            />
          </div>
          <Charities />
        </section>
      </main>
    </Fragment>
  );
}
