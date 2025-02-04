--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: location; Type: TABLE; Schema: public; Owner: andrew
--

CREATE TABLE public.location (
    location_id integer NOT NULL,
    city_state character varying(500) NOT NULL,
    country character varying(50) NOT NULL,
    longitude numeric(10,7) NOT NULL,
    latitude numeric(10,7) NOT NULL
);


ALTER TABLE public.location OWNER TO andrew;

--
-- Name: location_location_id_seq; Type: SEQUENCE; Schema: public; Owner: andrew
--

CREATE SEQUENCE public.location_location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.location_location_id_seq OWNER TO andrew;

--
-- Name: location_location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: andrew
--

ALTER SEQUENCE public.location_location_id_seq OWNED BY public.location.location_id;


--
-- Name: weather; Type: TABLE; Schema: public; Owner: andrew
--

CREATE TABLE public.weather (
    weather_id integer NOT NULL,
    temperature_fahrenheit numeric(5,2) NOT NULL,
    feels_like_fahrenheit numeric(5,2) NOT NULL,
    pressure integer NOT NULL,
    humidity numeric(4,2) NOT NULL,
    location_id integer NOT NULL,
    datetime timestamp with time zone,
    min_temp numeric(5,2) NOT NULL,
    max_temp numeric(5,2) NOT NULL
);


ALTER TABLE public.weather OWNER TO andrew;

--
-- Name: weather_weather_id_seq; Type: SEQUENCE; Schema: public; Owner: andrew
--

CREATE SEQUENCE public.weather_weather_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.weather_weather_id_seq OWNER TO andrew;

--
-- Name: weather_weather_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: andrew
--

ALTER SEQUENCE public.weather_weather_id_seq OWNED BY public.weather.weather_id;


--
-- Name: location location_id; Type: DEFAULT; Schema: public; Owner: andrew
--

ALTER TABLE ONLY public.location ALTER COLUMN location_id SET DEFAULT nextval('public.location_location_id_seq'::regclass);


--
-- Name: weather weather_id; Type: DEFAULT; Schema: public; Owner: andrew
--

ALTER TABLE ONLY public.weather ALTER COLUMN weather_id SET DEFAULT nextval('public.weather_weather_id_seq'::regclass);


--
-- Name: location location_pkey; Type: CONSTRAINT; Schema: public; Owner: andrew
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT location_pkey PRIMARY KEY (location_id);


--
-- Name: location unique_city_state; Type: CONSTRAINT; Schema: public; Owner: andrew
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT unique_city_state UNIQUE (city_state);


--
-- Name: weather weather_pkey; Type: CONSTRAINT; Schema: public; Owner: andrew
--

ALTER TABLE ONLY public.weather
    ADD CONSTRAINT weather_pkey PRIMARY KEY (weather_id);


--
-- Name: weather fk_location; Type: FK CONSTRAINT; Schema: public; Owner: andrew
--

ALTER TABLE ONLY public.weather
    ADD CONSTRAINT fk_location FOREIGN KEY (location_id) REFERENCES public.location(location_id);


--
-- PostgreSQL database dump complete
--

