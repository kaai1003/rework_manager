PGDMP     ,                    }        	   rework_db    13.19    13.19      �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16394 	   rework_db    DATABASE     X   CREATE DATABASE rework_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en-GB';
    DROP DATABASE rework_db;
                postgres    false            �            1259    16437    failures    TABLE     �   CREATE TABLE public.failures (
    id character varying NOT NULL,
    failure character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.failures;
       public         heap    postgres    false            �            1259    16427    lines    TABLE     �  CREATE TABLE public.lines (
    id character varying NOT NULL,
    project character varying NOT NULL,
    famille character varying NOT NULL,
    line integer NOT NULL,
    car_type character varying NOT NULL,
    superviseur character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.lines;
       public         heap    postgres    false            �            1259    16447    process    TABLE     �   CREATE TABLE public.process (
    id character varying NOT NULL,
    process character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.process;
       public         heap    postgres    false            �            1259    16417    projects    TABLE     I  CREATE TABLE public.projects (
    id character varying NOT NULL,
    project character varying NOT NULL,
    famille character varying NOT NULL,
    car_type character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.projects;
       public         heap    postgres    false            �            1259    16407 	   reference    TABLE     n  CREATE TABLE public.reference (
    id character varying NOT NULL,
    ref character varying NOT NULL,
    project character varying NOT NULL,
    famille character varying NOT NULL,
    car_type character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.reference;
       public         heap    postgres    false            �            1259    16477    reworkdetails    TABLE     8  CREATE TABLE public.reworkdetails (
    id character varying NOT NULL,
    ref character varying NOT NULL,
    project character varying NOT NULL,
    famille character varying NOT NULL,
    car_type character varying NOT NULL,
    line integer NOT NULL,
    superviseur character varying NOT NULL,
    reworkcard character varying NOT NULL,
    reworkfailure character varying NOT NULL,
    failuredetails character varying NOT NULL,
    processfailure character varying NOT NULL,
    reworktable integer NOT NULL,
    reworker character varying NOT NULL,
    quality character varying NOT NULL,
    status character varying NOT NULL,
    reworkduration double precision NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
 !   DROP TABLE public.reworkdetails;
       public         heap    postgres    false            �            1259    16467 	   reworkers    TABLE        CREATE TABLE public.reworkers (
    id character varying NOT NULL,
    name character varying NOT NULL,
    matricule character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.reworkers;
       public         heap    postgres    false            �            1259    16457    reworktables    TABLE     �   CREATE TABLE public.reworktables (
    id character varying NOT NULL,
    nr_table integer NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
     DROP TABLE public.reworktables;
       public         heap    postgres    false            �            1259    16395    users    TABLE     D  CREATE TABLE public.users (
    id character varying NOT NULL,
    username character varying NOT NULL,
    password character varying NOT NULL,
    role character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.users;
       public         heap    postgres    false            �          0    16437    failures 
   TABLE DATA           G   COPY public.failures (id, failure, created_at, updated_at) FROM stdin;
    public          postgres    false    204   "*       �          0    16427    lines 
   TABLE DATA           j   COPY public.lines (id, project, famille, line, car_type, superviseur, created_at, updated_at) FROM stdin;
    public          postgres    false    203   ?*       �          0    16447    process 
   TABLE DATA           F   COPY public.process (id, process, created_at, updated_at) FROM stdin;
    public          postgres    false    205   \*       �          0    16417    projects 
   TABLE DATA           Z   COPY public.projects (id, project, famille, car_type, created_at, updated_at) FROM stdin;
    public          postgres    false    202   y*       �          0    16407 	   reference 
   TABLE DATA           `   COPY public.reference (id, ref, project, famille, car_type, created_at, updated_at) FROM stdin;
    public          postgres    false    201   �*       �          0    16477    reworkdetails 
   TABLE DATA           �   COPY public.reworkdetails (id, ref, project, famille, car_type, line, superviseur, reworkcard, reworkfailure, failuredetails, processfailure, reworktable, reworker, quality, status, reworkduration, created_at, updated_at) FROM stdin;
    public          postgres    false    208   �*       �          0    16467 	   reworkers 
   TABLE DATA           P   COPY public.reworkers (id, name, matricule, created_at, updated_at) FROM stdin;
    public          postgres    false    207   �*       �          0    16457    reworktables 
   TABLE DATA           L   COPY public.reworktables (id, nr_table, created_at, updated_at) FROM stdin;
    public          postgres    false    206   �*       �          0    16395    users 
   TABLE DATA           U   COPY public.users (id, username, password, role, created_at, updated_at) FROM stdin;
    public          postgres    false    200   
+       f           2606    16446    failures failures_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.failures
    ADD CONSTRAINT failures_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.failures DROP CONSTRAINT failures_pkey;
       public            postgres    false    204            d           2606    16436    lines lines_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.lines
    ADD CONSTRAINT lines_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.lines DROP CONSTRAINT lines_pkey;
       public            postgres    false    203            h           2606    16456    process process_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.process
    ADD CONSTRAINT process_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.process DROP CONSTRAINT process_pkey;
       public            postgres    false    205            b           2606    16426    projects projects_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.projects DROP CONSTRAINT projects_pkey;
       public            postgres    false    202            `           2606    16416    reference reference_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.reference
    ADD CONSTRAINT reference_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.reference DROP CONSTRAINT reference_pkey;
       public            postgres    false    201            n           2606    16486     reworkdetails reworkdetails_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.reworkdetails
    ADD CONSTRAINT reworkdetails_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.reworkdetails DROP CONSTRAINT reworkdetails_pkey;
       public            postgres    false    208            l           2606    16476    reworkers reworkers_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.reworkers
    ADD CONSTRAINT reworkers_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.reworkers DROP CONSTRAINT reworkers_pkey;
       public            postgres    false    207            j           2606    16466    reworktables reworktables_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.reworktables
    ADD CONSTRAINT reworktables_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.reworktables DROP CONSTRAINT reworktables_pkey;
       public            postgres    false    206            \           2606    16404    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    200            ^           2606    16406    users users_username_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);
 B   ALTER TABLE ONLY public.users DROP CONSTRAINT users_username_key;
       public            postgres    false    200            �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �     