%global packname  kernlab
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.9.18
Release:          1
Summary:          Kernel-based Machine Learning Lab
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/kernlab_0.9-18.tar.gz
Requires:         R-methods 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
Kernel-based machine learning methods for classification, regression,
clustering, novelty detection, quantile regression and dimensionality
reduction. Among other methods kernlab includes Support Vector Machines,
Spectral Clustering, Kernel PCA and a QP solver.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
