import streamlit as st
from PIL import Image
import meta


# pylint: disable=line-too-long
def write():
    st.markdown(
        "<h1 style='text-align: justify; font-family: serif; font-size: 36px;color: black;font-weight: bold;'>Intro</h1",unsafe_allow_html=True)
    st.markdown(
        "<h4 style='text-align: justify; font-family: serif; font-size: 18px;color: black;font-weight: normal;'>To be able to talk to and hear one another has been fundamental to human evolution. This ability has led to the richness and diversity of human cultures which in turn has given rise to thousands of different languages and dialects, each with their own unique histories. For most of human history, our ability to communicate between different cultures and societies has been extremely limited. Clear communication often allows for cooperation and development, whilst a lack of this can lead to ignorance, fear, and even hatred. It is no surprise or coincidence that as communication barriers amongst our species have come down, intercultural cooperation and global development have increased.</h4",
        unsafe_allow_html=True)


    st.markdown(
        "<h4 style='text-align: justify; font-family: serif; font-size: 18px;color: black;font-weight: normal;'>Until recent decades, translation between languages was restricted to a select group of a population, often having the rare fortune of receiving a high-level education, that could afford to dedicate themselves to the study of languages. Through the rise of communication technologies over the 20th century, most notably the internet, we have experienced the rapid democratisation communication. Anyone with access to the internet can  now translate any language instantly, and anyone that would like to learn another language has free access to thousands of educational resources.</h4",
        unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: justify; font-family: serif; font-size: 18px;color: black;font-weight: normal;'>However, we believe this is merely the beginning, and, whilst this ranks amongst humanity’s greatest uses of technology, there are still vast numbers of the human population that do not have the privilege of being able to communicate through ‘conventional’ language. And as a result many of these people are overlooked when it comes to these breakthroughs in human communication.</h4",unsafe_allow_html=True)

    st.markdown(
        "<h1 style='text-align: justify; font-family: serif; font-size: 36px;color: black;font-weight: bold;'>Sign-Language </h1",
        unsafe_allow_html=True)

    st.markdown(
        "<h4 style='text-align: justify; font-family: serif; font-size: 18px;color: black;font-weight: normal;'>It is easy for those of us unexposed to hearing difficulties to be unaware of the sheer scale of the issue. According to the WHO, over 5% of the world’s population – or around 460 million people – require rehabilitation to address their ‘disabling’ hearing loss (432 million adults and 34 million children).  It is estimated that by 2050 over 700 million people – or 1 in every 10 people – will have disabling hearing loss.</h4",
        unsafe_allow_html=True)
    st.markdown(
        "<h4 style='text-align: justify; font-family: serif; font-size: 18px;color: black;font-weight: normal;'>In developing countries, children with hearing loss and deafness often do not receive schooling. Adults with hearing loss also have a much higher unemployment rate. Among those who are employed, a higher percentage of people with hearing loss are in the lower grades of employment compared with the general workforce.</h4",
    unsafe_allow_html=True)
    st.markdown(
        "<h4 style='text-align: justify; font-family: serif; font-size: 18px;color: black;font-weight: normal;'>WHO estimates that unaddressed hearing loss poses an annual global cost of US$ 980 billion.</h4",
    unsafe_allow_html=True)
    st.markdown(
        "<h4 style='text-align: justify; font-family: serif; font-size: 18px;color: black;font-weight: normal;'>The primary way that those with hearing difficulties can communicate with one another is through the use of sign languages.</h4",
    unsafe_allow_html=True)
    st.markdown(
        "<h4 style='text-align: justify; font-family: serif; font-size: 18px;color: black;font-weight: normal;'>A couple of common misconceptions are that sign languages are relatively simple and that there are only a few, universal sign languages used around the world. This is far from correct. In fact the SIGN-HUB Atlas of Sign Language Structures lists over 200 languages and notes that there are more which have not been documented or discovered yet. In linguistic terms, sign languages are as rich and complex as any spoken language, and are full-fledged natural languages with their own grammar and lexicon.  Sign languages are not universal and they are not mutually intelligible with each other, although there are also striking similarities among sign languages.</h4",
    unsafe_allow_html=True)

    st.markdown(
        "<h4 style='text-align: justify; font-family: serif; font-size: 18px;color: black;font-weight: normal;'>Sign languages generally do not have any linguistic relation to the spoken languages of the lands in which they arise. The correlation between sign and spoken languages is complex and varies depending on the country more than the spoken language. For example, Australia, Canada, New Zealand, the UK and the US all have English as their dominant language, but American Sign Language (ASL), used in the US and English-speaking Canada, is derived from French Sign Language whereas the other three countries use varieties of British, Australian and New Zealand Sign Language, which is unrelated to ASL.</h4",
        unsafe_allow_html=True)
    st.markdown(
        "<h1 style='text-align: justify; font-family: serif; font-size: 36px;color: black;font-weight: bold;'>Our Mission</h1",unsafe_allow_html=True)

    st.markdown(
        "<h4 style='text-align: justify; font-family: serif; font-size: 18px;color: black;font-weight: normal;'>From identity detection to autonomous vehicles, ‘Computer Vision’, enabled by deep learning CNN models, is becoming increasingly ubiquitous. We see an immense opportunity to utilise the power of this technology to make communication with those with hearing difficulties just as seamless as any other form of translation. The aim of SignSight is to give any user the ability to translate and learn a wide array of Sign-languages easily and effectively. Starting with American and Arabic Sign-language we have successfully implemented a user-friendly application that is able to translate any letter or number instantly when shown the corresponding hand signal through the camera. We have also added a flashcard system to help users learn and retain the knowledge of the Sign-language of their choice.</h4",
        unsafe_allow_html=True)
    st.markdown(
        "<h4 style='text-align: justify; font-family: serif; font-size: 18px;color: black;font-weight: normal;'>Whilst there are other models and companies that aim to do this too, and have achieved this to a certain extent, our research has taught us that most of this has been focused solely on ASL, and mainly targeted at adults. Democratisation of communication is a fundamental value for us, and as such we foresee SignSight as a platform that expands Sign-language access to all regions, and all ages. SignSight will incorporate a wide range of different Sign-languages, as well as providing a service that will aim to teach kids, as well as adults, in a fun, interactive, structured manner, combining the capabilities of both educational AI and Computer Vision.</h4",
        unsafe_allow_html=True)
