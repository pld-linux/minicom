Summary:	TTY mode communications package ala Telix
Summary(de):	TTY-Modus-Kommunikationspaket (Дhnlich Telix)
Summary(es):	Paquete de comunicaciones modo texto a la Telix
Summary(fr):	Package de communication en mode terminal Ю la Telix
Summary(pl):	Program komunikacyjny (podobny do Telix-a)
Summary(pt_BR):	Pacote de comunicaГУes modo texto a la Telix
Summary(tr):	Telix benzeri, TTY kipi iletiЧim paketi
Summary(ru):	Коммуникационный пакет типа Telix для текстового режима
Summary(uk):	Комун╕кац╕йний пакет типу Telix для текстового режиму
Summary(zh_CN):	р╩╦Жнд╠╬╫ГцФ╣д╣Вйт╫Б╣ВфВ©ьжффВ╨мжу╤кдёдБфВ║ё
Name:		minicom
Version:	1.83.1
Release:	14
License:	GPL
Group:		Applications/Communications
Source0:	http://www.pp.clinet.fi/~walker/%{name}-%{version}.src.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}.patch
Patch3:		%{name}.uninitialized.patch
Patch4:		%{name}-make.patch
Patch5:		%{name}-lrzsz.patch
Patch6:		%{name}-time.patch
Patch7:		%{name}-logging.patch
Patch8:		%{name}-ko.patch
Patch9:		%{name}-format-string-vuln.patch
Patch10:	%{name}-umask.patch
Patch11:	%{name}-drop-privs.patch
Patch12:	%{name}-check_exec.patch
URL:		http://www.pp.clinet.fi/~walker/minicom.html
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minicom is a communications program that resembles the MSDOS Telix
somewhat. It has a dialing directory, color, full ANSI and VT100
emulation, an (external) scripting language and more.

%description -l de
Minicom ist ein Kommunikationsprogramm, das дhnlichkeiten mit Telix
unter MSDOS aufweist. Es enthДlt ein WДhlverzeichnis, Farbe,
vollstДndige ANSI- und VT100-Emulation, eine (externe) Scriptsprache
usw.

%description -l es
Minicom es un programa de comunicaciСn que se parece con el Telix del
MSDOS. Tiene un directorio de marcado, color, emulaciСn completa ANSI
y VT100, y un lenguaje externo de sxripts y mail.

%description -l fr
Minicom est un programme de communication ressemblant a Telix sous
MSDOS. Il a un rИpertoire de numИrotation, des couleurs, une Иmualtion
ANSI et VT100, un langage de script externe et plus encore.

%description -l pl
Minicom jest programem komunikacyjnym, przypominaj╠cym DOSowy program
Telix. Posiada ksi╠©kЙ telefoniczn╠, emulacjЙ terminali ANSI i VT100,
zewnЙtrzny jЙzyk skryptowy, obsЁugЙ kolorСw i wiele innych wЁasno╤ci.

%description -l pt_BR
Minicom И um programa de comunicaГЦo que parece com o Telix do MSDOS.
Tem um diretСrio de discagem, cor, emulaГЦo completa ANSI e VT100, e
uma linguagem externa de scripts e mail.

%description -l tr
Minicom, MSDOS Telix programЩna benzeyen bir iletiЧim programЩdЩr.
Numara Гevirme dizini, renk, tam ANSI uyumu ve VT100 ЖykЭnЭmЭ ile
script gibi Жzellikleri vardЩr.

%description -l ru
Minicom - это коммуникационная программа, в чем-то похожая на MSDOS
Telix. Она включает телефонную книгу, цвет, полную поддержку ANSI и
VT100, внешний язык скриптов и многое другое.

%description -l uk
Minicom - це комун╕кац╕йна програма, чимось схожа на MSDOS Telix. Вона
м╕стить телефонну книгу, кол╕р, повну п╕дтримку ANSI та VT100, зовн╕шю
мову скрипт╕в та багато ╕ншого.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
%{__make} -C src LIBDIR="%{_sysconfdir}/minicom"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/{profile.d,minicom} \
	$RPM_BUILD_ROOT%{_applnkdir}/System \
	$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/locale,%{_mandir}/man1}

%{__make} -C src DESTDIR="$RPM_BUILD_ROOT" \
	LIBDIR="%{_sysconfdir}/minicom" \
	MANDIR="%{_mandir}/man1" install

cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/minicom/minirc.dfl
pu minit            ~^M~ATZ^M~
pu mreset           ~^M~ATZ^M~
EOF

cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/minicom.sh
MINICOM="-L"
if [ "\$TERM" = linux -o "\$TERM" = xterm-color -o "\$TERM" = vt220 ] ; then
	MINICOM="\$MINICOM -c on"
fi
export MINICOM
EOF

cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/minicom.csh
setenv MINICOM "-L"
if ( "\$TERM" == linux || "\$TERM" == xterm-color || "\$TERM" == vt220 ) \
	setenv MINICOM "\$MINICOM -c on"
EOF

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/System
bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf demos/* doc/* tables/*

%find_lang minicom

%clean
rm -rf $RPM_BUILD_ROOT

%files -f minicom.lang
%defattr(644,root,root,755)
%doc demos doc tables

%attr(750,root,ttyS) %dir %{_sysconfdir}/minicom
%attr(640,root,ttyS) %config %verify(not size md5 mtime) %{_sysconfdir}/minicom/*
%attr(755,root,root) %{_sysconfdir}/profile.d/minicom.sh
%attr(755,root,root) %{_sysconfdir}/profile.d/minicom.csh

%attr(755,root,root) %{_bindir}/minicom

%attr(755,root,root) %{_bindir}/runscript
%attr(755,root,root) %{_bindir}/xminicom
%attr(755,root,root) %{_bindir}/ascii-xfr

%{_applnkdir}/System/minicom.desktop
%{_mandir}/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(pl) %{_mandir}/pl/man1/*
