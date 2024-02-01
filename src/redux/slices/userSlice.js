import { createSlice } from "@reduxjs/toolkit";

const userSlice = createSlice({
  name: 'auth',
  initialState: { user: null },
  reducers: {
    setSignIn: (state, action) => {
      const { user } = action.payload
      state.user = user
    },
    setSignOut: (state, action) => {
      state.user = null
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