Summary:	TTY mode communications package ala Telix
Summary(de):	TTY-Modus-Kommunikationspaket (ähnlich Telix)
Summary(fr):	Package de communication en mode terminal à la Telix
Summary(pl):	Program komunikacyjny (podobny do Telix-a)
Summary(tr):	Telix benzeri, TTY kipi iletiþim paketi
Name:		minicom
Version:	1.83.0
Release:	1
License:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
URL:		http://www.pp.clinet.fi/~walker
Source0:	http://www.pp.clinet.fi/~walker/%{name}-%{version}.src.tar.gz
Source1:	%{name}.desktop
Source2:	http://www.pp.clinet.fi/~walker/%{name}.FAQ
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}.patch
Patch3:		%{name}.uninitialized.patch
Buildroot:	/tmp/%{name}-%{version}-root

%define		_applnkdir	%{_prefix}/X11R6/share/applnk
%description
Minicom is a communications program that resembles the MSDOS Telix
somewhat. It has a dialing directory, color, full ANSI and VT100 emulation,
an (external) scripting language and more.

%description -l de
Minicom ist ein Kommunikationsprogramm, das Ähnlichkeiten mit Telix  unter
MSDOS aufweist. Es enthält ein Wählverzeichnis, Farbe, vollständige ANSI-
und VT100-Emulation, eine (externe) Scriptsprache usw.

%description -l fr
Minicom est un programme de communication ressemblant a Telix sous MSDOS.
Il a un répertoire de numérotation, des couleurs, une émualtion ANSI et
VT100, un langage de script externe et plus encore.

%description -l pl
Minicom jest programem komunikacyjnym, przypominaj±cym DOSowy program
Telix. Posiada ksi±¿kê telefoniczn±, emulacjê terminali ANSI i VT100,
zewnêtrzny jêzyk skryptowy, obs³ugê kolorów i wiele innych zalet.

%description -l tr
Minicom, MSDOS Telix programýna benzeyen bir iletiþim programýdýr. Numara
çevirme dizini, renk, tam ANSI uyumu ve VT100 öykünümü ile script gibi
özellikleri vardýr.

%prep
%setup -q
%patch0 -p1 
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
LDFLAGS="-s"; export LDFLAGS
CFLAGS="$RPM_OPT_FLAGS" make -C src

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/{profile.d,minicom}
install -d $RPM_BUILD_ROOT%{_applnkdir}
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/locale,%{_mandir}/man1}

make -C src install R="$RPM_BUILD_ROOT" LIBDIR="%{_sysconfdir}/minicom" MANDIR="%{_mandir}/man1"

cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/minicom/minirc.dfl
pu minit            ~^M~ATZ^M~
pu mreset           ~^M~ATZ^M~
EOF

cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/minicom.sh
#!/bin/bash
MINICOM="-c on -m -L"
export MINICOM
EOF

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/minicom.desktop
install %{SOURCE2} .

strip $RPM_BUILD_ROOT%{_bindir}/* ||:

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* demos/* doc/* tables/* \
	minicom.FAQ

%find_lang minicom

%clean
rm -rf $RPM_BUILD_ROOT

%files -f minicom.lang
%defattr(644,root,root,755)
%doc demos doc tables minicom.FAQ.gz

%attr(750,root,root) %dir %{_sysconfdir}/minicom
%attr(640,root,root) %config %verify(not size md5 mtime) %{_sysconfdir}/minicom/*
%attr(755,root,root) %{_sysconfdir}/profile.d/minicom.sh

%attr(755,root,root) %{_bindir}/minicom

%attr(755,root,root) %{_bindir}/runscript
%attr(755,root,root) %{_bindir}/xminicom
%attr(755,root,root) %{_bindir}/ascii-xfr

%{_applnkdir}/minicom.desktop
%{_mandir}/man1/*
