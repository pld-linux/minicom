Summary:	TTY mode communications package ala Telix
Summary(de):	TTY-Modus-Kommunikationspaket (ähnlich Telix)
Summary(fr):	Package de communication en mode terminal à la Telix
Summary(pl):	Program komunikacyjny (podobny do Telix-a)
Summary(tr):	Telix benzeri, TTY kipi iletiþim paketi
Name:		minicom
Version:	1.82.1
Release:	3
Copyright:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
URL:		http://www.pp.clinet.fi/~walker
Source0:	%{name}-%{version}.src.tar.gz
Source1:	%{name}.wmconfig
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}.patch
Patch3:		%{name}.uninitialized.patch
Buildroot:	/tmp/buildroot-%{name}-%{version}

%description
Minicom is a communications program that resembles the MSDOS Telix
somewhat. It has a dialing directory, color, full ANSI and VT100
emulation, an (external) scripting language and more.

%description -l de
Minicom ist ein Kommunikationsprogramm, das Ähnlichkeiten mit Telix 
unter MSDOS aufweist. Es enthält ein Wählverzeichnis, Farbe, vollständige ANSI-
und VT100-Emulation, eine (externe) Scriptsprache usw.

%description -l fr
Minicom est un programme de communication ressemblant a Telix sous
MSDOS. Il a un répertoire de numérotation, des couleurs, une émualtion
ANSI et VT100, un langage de script externe et plus encore.

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
LDFLAGS=-s make -C src CC="gcc $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{X11/wmconfig,profile.d,minicom}
install -d $RPM_BUILD_ROOT{/usr/{bin,share/locale},%{_mandir}/man1}

make -C src install R="$RPM_BUILD_ROOT" LIBDIR="/etc/minicom" MANDIR="%{_mandir}/man1"

cat << EOF > $RPM_BUILD_ROOT/etc/minicom/minirc.dfl
pu minit            ~^M~ATZ^M~
pu mreset           ~^M~ATZ^M~
EOF

cat << EOF > $RPM_BUILD_ROOT/etc/profile.d/minicom.sh
#!/bin/bash
MINICOM="-c on -m -L"
export MINICOM
EOF

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/minicom

strip $RPM_BUILD_ROOT/usr/bin/* ||:

bzip2 -9 $RPM_BUILD_ROOT%{_mandir}/man1/* demos/* doc/* tables/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc demos doc tables

%attr(750,root,root) %dir /etc/minicom
%attr(640,root,root) %config %verify(not size md5 mtime) /etc/minicom/*
%attr(755,root,root) /etc/profile.d/minicom.sh

%attr(755,root,root) /usr/bin/minicom

%attr(755,root,root) /usr/bin/runscript
%attr(755,root,root) /usr/bin/xminicom
%attr(755,root,root) /usr/bin/ascii-xfr

%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/minicom
%attr(644,root, man) %{_mandir}/*

%lang(fi) /usr/share/locale/fi_FI/LC_MESSAGES/*.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/*.mo
%lang(pl) /usr/share/locale/pl/LC_MESSAGES/*.mo
%lang(pt) /usr/share/locale/pt_BR/LC_MESSAGES/*.mo

%changelog
* Tue Jun 29 1999 Michal Margula <alchemyx@pld.org.pl>
  [1.82.1-3]
- fixed for compiling with ncurses
- FHS 2.0 ready
- minor fixes in spec

* Wed Feb 03 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [1.82.1-1d]
- new upstream release

* Mon Jan 11 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [1.82-3d]
- added 1.82.1 pre patch ;>
- updated pl translation in this patch

* Thu Dec 24 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [1.82-2d]
- added defaul initstring,
- added /etc/profile.d/minicom.sh,
- added uninitialized patch.

* Sat Oct 10 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [1.82-1d]
- translations modified for pl,
- updated to 1.82.
- defined files permission,
- allow building from non root account,
- moved changelog to the end of spec.

* Tue Jun 30 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.81-7d]
- build against GNU libc-2.1.

* Sun May 10 1998 Cristian Gafton <gafton@redhat.com>
- security fixes (alan cox, but he forgot about the changelog)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- BuildRoot; updated .make patch to cope with the buildroot
- fixed the spec file

* Tue May 06 1998 Michael Maher <mike@redhat.com>
- update of package (1.81)

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added wmconfig entries

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed source url

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
