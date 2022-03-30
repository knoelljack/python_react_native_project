import { View, Text, TextInput, StyleSheet } from 'react-native'
import React from 'react'
import Form from '../profile/Form'

const Login = ({ navigation }) => {

    return (
        <View>
            <Form navigation={navigation} />
            {/* add the login form here instead of the screen */}
        </View>
    )
}
// const styles = StyleSheet.create({
//     root: {
//         padding: 10,
//     },
//     heading: {
//         fontSize: 28,
//         fontWeight: 'bold',
//         textAlign: 'center',
//     },
//     row: {
//         marginVertical: 5,
//     },
//     label: {
//         fontSize: 16,
//         fontWeight: 'bold',
//         marginLeft: 5
//     },
//     input: {
//         height: 40,
//         backgroundColor: 'white',
//         padding: 5,
//         marginVertical: 5,
//         borderRadius: 20,
//     },
//     card: {
//         backgroundColor: 'white',
//         padding: 18,
//         paddingVertical: 35,
//         borderRadius: 25,
//         margin: 15,
//         justifyContent: 'center'
//     },
//     shadow: {
//         shadowColor: '#171717',
//         shadowOffset: { width: 2, height: 2 },
//         shadowOpacity: 0.2,
//         shadowRadius: 5,
//     },
//     error: { color: 'red' },
//     button: {
//         backgroundColor: 'turquoise',
//         padding: 8,
//         borderRadius: 20,
//         marginVertical: 10,
//         alignItems: 'center',
//     },
//     buttonText: {
//         textAlign: 'center',
//         justifyContent: 'center',
//         color: 'white',
//         fontWeight: '700'
//     }
// })
export default Login