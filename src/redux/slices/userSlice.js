import { createSlice } from "@reduxjs/toolkit";

const userSlice = createSlice({
  name: 'auth',
  initialState: { user: {}, },
  reducers: {
    setSignIn: (state, action) => {
      state.user = {...state.user, ...action.payload}
    },
    setSignOut: (state) => {
      state.user = {}
    }
  },
})

export const { setSignIn, setSignOut } = userSlice.actions
export default userSlice.reducer

export const selectCurrentUser = (state) => state.auth.user

// import { createSlice } from "@reduxjs/toolkit";

// const initialState = {
//   user: {},
//   isLoggedIn: false,
// }

// const userSlice = createSlice({
//   name: 'userSlice',
//   initialState,
//   reducers: {
//     signIn: (state, action) => {
//       state.user = {...state.user, ...action.payload}
//       state.isLoggedIn = true
//     },
//     signOut: (state) => {
//       state.user = {}
//       state.isLoggedIn = false
//     }
//   }
// })

// export const { signIn, signOut } = userSlice.actions
// export default userSlice.reducer


// import { createSlice } from "@reduxjs/toolkit";

// const userSlice = createSlice({
//   name: 'auth',
//   initialState: { user: "guest", },
//   reducers: {
//     setSignIn: (state, action) => {
//       const { user } = action.payload
//       state.user = user
//     },
//     setSignOut: (state, action) => {
//       state.user = "guest"
//     }
//   },
// })

// export const { setSignIn, setSignOut } = userSlice.actions
// export default userSlice.reducer

// export const selectCurrentUser = (state) => state.auth.user

// const userSlice = createSlice({
//   name: 'auth',
//   initialState: { user: "guest", },
//   reducers: {
//     setSignIn: (state, action) => {
//       state.user = {...state.user, ...action.payload}
//     },
//     setSignOut: (state, action) => {
//       state.user = "guest"
//     }
//   },
// })

// export const { setSignIn, setSignOut } = userSlice.actions
// export default userSlice.reducer

// export const selectCurrentUser = (state) => state.auth.user

// const initialState = {
//   user: null,
//   isLoggedIn: false,
// }

// const userSlice = createSlice({
//   name: 'auth',
//   initialState,
//   reducers: {
//     setSignIn: (state, action) => {
//       state.user = {...state.user, ...action.payload}
//       // state.isLoggedIn = true
//     },
//     setSignOut: (state) => {
//       state.user = null
//       // state.isLoggedIn = false
//     }
//   }
// })

// import { createSlice } from "@reduxjs/toolkit";

// const userSlice = createSlice({
//   name: 'auth',
//   initialState: { user: "guest", },
//   reducers: {
//     setSignIn: (state, action) => {
//       state.user = {...state.user, ...action.payload}
//     },
//     setSignOut: (state, action) => {
//       state.user = "guest"
//     }
//   },
// })

// export const { setSignIn, setSignOut } = userSlice.actions
// export default userSlice.reducer

// export const selectCurrentUser = (state) => state.auth.user