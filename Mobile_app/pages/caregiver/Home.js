import React, { useEffect, useState } from "react";
import { StyleSheet, Text, TouchableOpacity, View, Dimensions } from "react-native";
import MapViewDirections from 'react-native-maps-directions';
import { LogBox } from 'react-native';
LogBox.ignoreLogs(['new NativeEventEmitter']); // Ignore log notification by message
LogBox.ignoreAllLogs()
import { FontAwesome5,FontAwesome6, MaterialCommunityIcons, Feather } from '@expo/vector-icons';
import { Circle, Polyline, Marker } from "react-native-maps";
import MapView from '../../components/Map/MapView'
import useUserStore from "../../store/userStore";
import Loader from "../../components/Loader";
import Colors from "../../constants/Colors";
import useMapContext from "../../components/Map/useMapContext";
import { useTranslation } from 'react-i18next'

const { width, height } = Dimensions.get('window');
const GOOGLE_MAPS_APIKEY ='AIzaSyAaCWjzUJ1XziqSuWycOTNorOmfe2swDIc';

const Home = ({ navigation }) => {
    const currentUser = useUserStore((state) => state.currentUser)
    const userCoords = useUserStore((state) => state.userCoords)
    const { map, setMap } = useMapContext()
    const {t} = useTranslation()
    const [distanceTime, setDistanceTime] = useState({
        distance: null,
        duration: null
    })
    const [direction,setDirection] = useState(false)
    const visionUser = useUserStore((state) => state.sixthSenseUser)
    print(visionUser)
    function navigationCenter() { 
        setDirection((state) => !state)
    }
    
    if (currentUser) {
        return (
            <View style={{ flex: 1 }}>
                <MapView>
                    {direction && (
                        <MapViewDirections
                            origin={userCoords}
                            destination={visionUser?.coords}
                            apikey={GOOGLE_MAPS_APIKEY}
                            onReady={result => {
                                setDistanceTime({
                                    distance: result.distance,
                                    duration: result.duration
                                })
                                if (map)
                                    map.fitToCoordinates(result.coordinates, {
                                        edgePadding: {
                                            right: (width / 20),
                                            bottom: (height / 20),
                                            left: (width / 20),
                                            top: (height / 20),
                                        }
                                    });
                        
                            }}
                            strokeWidth={3}
                            strokeColor={Colors.three}
                                        
                        />
                    )}
                    <Circle radius={visionUser?.radius} center={visionUser?.geoFence} strokeWidth={2} strokeColor={Colors.three} fillColor={visionUser?.inBound ? "rgba(144, 210, 109, 0.5)": "rgba(244,0,0, 0.5)"} />
                    <Polyline coordinates={[{ latitude: visionUser?.geoFence?.latitude, longitude: visionUser?.geoFence?.longitude }, { latitude: visionUser?.coords.latitude, longitude: visionUser?.coords.longitude }]} strokeWidth={3} strokeColor={Colors.three} lineDashPattern={[1, 1]} style={{ position: 'relative' }} />
                    <Marker coordinate={visionUser?.geoFence}>
                <MaterialCommunityIcons name="map-marker-radius" size={34} color={Colors.three} />
                </Marker>
                </MapView>
                {direction && (
                    <View style={styles.dataContainer}>
                        <Text style={styles.dataText}>{distanceTime.distance?.toFixed(2)} Km</Text>
                        <Text style={styles.dataText}>{distanceTime.duration?.toFixed(2)} Min</Text>
                    </View>
                )}
                    <View style={{...styles.statusContainer, backgroundColor:visionUser?.inBound? Colors.two : 'red'}}>
                    <View style={{paddingVertical: 4, paddingHorizontal: 10, alignItems: 'center', justifyContent: 'center', backgroundColor: Colors.one, borderRadius: 50}}>
                    <FontAwesome6 name="person" size={32} color={visionUser?.inBound? Colors.three : 'red'}/>
                    </View>
                    <Text style={{ ...styles.text, color: Colors.one}}>{visionUser?.inBound ? `${t("Inside the safe zone")}` :  `${t("Outside the safe zone")}`}</Text>
                </View>
                <TouchableOpacity style={styles.navigationCenter} onPress={navigationCenter} >
                    <FontAwesome5 name="route" size={32} color={Colors.three} />
                </TouchableOpacity>
                <TouchableOpacity style={styles.geoFence} onPress={() => {
                    navigation.navigate('GeoFence')
                }} >
              <Feather name="alert-circle" size={32} color={Colors.three} />
                </TouchableOpacity>
            </View>
        )
    } else {
            return <Loader/>
        }

}

export default Home

const styles = StyleSheet.create({
    navigationCenter: {
        position: 'absolute',
        bottom: 15,
        right: 130,
        zIndex: 2,
    },
    geoFence: {
        position: 'absolute',
        bottom: 15,
        left: 20
    },
    dataContainer: {
        position: 'absolute',
        bottom: 60,
        left: '50%',
        backgroundColor: Colors.two,
        padding: 10,
        borderRadius: 10,
        flexDirection: 'row',
        gap: 15,
        transform: [{translateX: -90}]
    },
    dataText: {
        color: Colors.one,
        fontSize: 18,
    }, 
    statusContainer: {
        display: 'flex',
        flexDirection: 'row',
        alignItems: 'center',
        paddingVertical: 8,
        paddingHorizontal: 15,
        borderRadius: 20,
        gap: 20,
        position: 'absolute',
        top: 40,
        left: '50%',
        transform: [{translateX: -100}]
    }
})