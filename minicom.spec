# TODO:
# - move ascii-xfr to separate package (can be used by picocom and others)
Summary:	TTY mode communications package ala Telix
Summary(de.UTF-8):	TTY-Modus-Kommunikationspaket (ähnlich Telix)
Summary(es.UTF-8):	Paquete de comunicaciones modo texto a la Telix
Summary(fi.UTF-8):	Tietoliikenneohjelma, kuten Telix
Summary(fr.UTF-8):	Package de communication en mode terminal à la Telix
Summary(pl.UTF-8):	Program komunikacyjny (podobny do Teliksa)
Summary(pt_BR.UTF-8):	Pacote de comunicações modo texto a la Telix
Summary(ru.UTF-8):	Коммуникационный пакет типа Telix для текстового режима
Summary(tr.UTF-8):	Telix benzeri, TTY kipi iletişim paketi
Summary(uk.UTF-8):	Комунікаційний пакет типу Telix для текстового режиму
Summary(zh_CN.UTF-8):	一个文本界面的调试解调器控制器和终端模拟器。
Name:		minicom
Version:	2.5
Release:	2
License:	GPL v2
Group:		Applications/Communications
Source0:	http://alioth.debian.org/download.php/3487/%{name}-%{version}.tar.gz
# Source0-md5:	a5117d4d21e2c9e825edb586ee2fe8d2
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	93ca30842bce63473004570b6b30be25
Patch0:		%{name}-fromsnap.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}-check_exec.patch
Patch3:		%{name}-man_no_ko.patch
Patch4:		%{name}-tinfo.patch
URL:		http://alioth.debian.org/projects/minicom/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-devel >= 0.14.1
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	sed >= 4.0
Requires:	/usr/bin/tput
Requires:	setup >= 2.6.1-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minicom is a communications program that resembles the MSDOS Telix
somewhat. It has a dialing directory, color, full ANSI and VT100
emulation, an (external) scripting language and more.

%description -l de.UTF-8
Minicom ist ein Kommunikationsprogramm, das Ähnlichkeiten mit Telix
unter MSDOS aufweist. Es enthält ein Wählverzeichnis, Farbe,
vollständige ANSI- und VT100-Emulation, eine (externe) Scriptsprache
usw.

%description -l es.UTF-8
Minicom es un programa de comunicación que se parece con el Telix del
MSDOS. Tiene un directorio de marcado, color, emulación completa ANSI
y VT100, y un lenguaje externo de sxripts y mail.

%description -l fi.UTF-8
Minicom on MSDOS-Telixiä jossain määrin muistuttava
tietoliikenneohjelma. Ohjelmassa on mm. puhelinluettelo, värit, ANSI-
ja VT100-emulaatiot ja ulkoinen script-kieli.

%description -l fr.UTF-8
Minicom est un programme de communication ressemblant a Telix sous
MSDOS. Il a un répertoire de numérotation, des couleurs, une émualtion
ANSI et VT100, un langage de script externe et plus encore.

%description -l pl.UTF-8
Minicom jest programem komunikacyjnym, przypominającym DOS-owy program
Telix. Posiada książkę telefoniczną, emulację terminali ANSI i VT100,
zewnętrzny język skryptowy, obsługę kolorów i wiele innych własności.

%description -l pt_BR.UTF-8
Minicom é um programa de comunicação que parece com o Telix do MSDOS.
Tem um diretório de discagem, cor, emulação completa ANSI e VT100, e
uma linguagem externa de scripts e mail.

%description -l ru.UTF-8
Minicom - это коммуникационная программа, в чем-то похожая на MSDOS
Telix. Она включает телефонную книгу, цвет, полную поддержку ANSI и
VT100, внешний язык скриптов и многое другое.

%description -l tr.UTF-8
Minicom, MSDOS Telix programına benzeyen bir iletişim programıdır.
Numara çevirme dizini, renk, tam ANSI uyumu ve VT100 öykünümü ile
script gibi özellikleri vardır.

%description -l uk.UTF-8
Minicom - це комунікаційна програма, чимось схожа на MSDOS Telix. Вона
містить телефонну книгу, колір, повну підтримку ANSI та VT100, зовнішю
мову скриптів та багато іншого.

%prep
%setup -q
%undos po/pt_BR.po
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

rm -f po/stamp-po

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--sysconfdir="%{_sysconfdir}/minicom"

%{__make}

%{__rm} doc/*.old

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/profile.d,%{_sysconfdir}/minicom} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/locale,%{_mandir}/man1}

%{__make} DESTDIR="$RPM_BUILD_ROOT" \
	LIBDIR="%{_sysconfdir}/minicom" \
	MANDIR="%{_mandir}/man1" install

cat << 'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/minicom/minirc.dfl
pu minit            ~^M~ATZ^M~
pu mreset           ~^M~ATZ^M~
EOF

cat << 'EOF' > $RPM_BUILD_ROOT/etc/profile.d/minicom.sh
MINICOM="-l"
if [ "$TERM" ] && [ "`/usr/bin/tput colors 2>/dev/null`" != "-1" ] ; then
	MINICOM="$MINICOM -c on"
fi
export MINICOM
EOF

cat << 'EOF' > $RPM_BUILD_ROOT/etc/profile.d/minicom.csh
setenv MINICOM "-l"
if ( $?TERM ) then
	if ( "`/usr/bin/tput colors 2>/dev/null`" != "-1" ) \
		setenv MINICOM "$MINICOM -c on"
endif
EOF

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

# Prepare directories with doc files
# (nasty hack to avoid Makefiles & have docs splitted into dirs)
install -d rpm-doc/{extras,doc,tables}
cp -a extras/[hsu]* rpm-doc/extras
cp -a doc/* rpm-doc/doc
cp -a extras/tables/mc* rpm-doc/tables
%{__rm} rpm-doc/doc/Makefile*

%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.minicom-non-english-man-pages
%{__rm} $RPM_BUILD_ROOT%{_mandir}/minicom-pld_path.diff

%find_lang minicom

%clean
rm -rf $RPM_BUILD_ROOT

%files -f minicom.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README rpm-doc/{extras,doc,tables}

%attr(750,root,dialout) %dir %{_sysconfdir}/minicom
%attr(640,root,dialout) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/minicom/*
%attr(755,root,root) /etc/profile.d/minicom.sh
%attr(755,root,root) /etc/profile.d/minicom.csh

%attr(755,root,root) %{_bindir}/ascii-xfr
%attr(755,root,root) %{_bindir}/minicom
%attr(755,root,root) %{_bindir}/runscript
%attr(755,root,root) %{_bindir}/xminicom

%{_desktopdir}/minicom.desktop
%{_pixmapsdir}/minicom.png
%{_mandir}/man1/ascii-xfr.1*
%{_mandir}/man1/minicom.1*
%{_mandir}/man1/runscript.1*
%{_mandir}/man1/xminicom.1*
%lang(ko) %{_mandir}/ko/man1/*.1*
%lang(pl) %{_mandir}/pl/man1/*.1*
