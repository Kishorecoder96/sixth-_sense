import i18next from "i18next";
import { initReactI18next } from "react-i18next";

const resources = {
    en: {
      translation:  require('./en.json'),
    },
    hi: {
      translation: require('./hi.json'),
  },
  fr: {
    translation: require('./french.json'),
  },
  ko: {
    translation: require('./korean.json'),
  },
  es: {
    translation: require('./spanish.json'),
  }
  }
  
  i18next.use(initReactI18next).init({
    debug: false,
    lng: 'en',
    compatibilityJSON: 'v3',
    fallbackLng: 'en',
    resources,
  })
  
  export default i18next;