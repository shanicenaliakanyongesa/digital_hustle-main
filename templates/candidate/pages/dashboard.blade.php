<div class="page-own-content">
    <div class="da-row">
        <div class="da-col-xs-12">
            <div class="dash-card">
                <div class="search-bar-main">
                    <form action="{{ route('candidate.main-job-search') }}" method="POST" >
                        @csrf
                        <div class="search-bar-main-location">
                            <div class="search-bar-main-icon">
                                <span class="las la-map-marker"></span>
                            </div>
                            <div class="search-bar-main-select">
                                <select name="search_location" id="">
                                    <option>Around You</option>
                                    <option value="1">Location1</option>
                                    <option value="2">Location2</option>
                                    <option value="3">Location3</option>
                                    <option value="4">Location4</option>
                                    <option value="5">Location5</option>
                                </select>
                            </div>
                        </div>
                        <div class="search-bar-main-search-field">
                            <input type="text" name="search_bar_main_input" placeholder="Search by Title, Company or any job's keyword">
                        </div>
                        <div class="search-bar-main-buttons">
                            <div class="btn btn-blue3">
                                <span class="las la-stream"></span>
                                FILTER
                            </div>
                            <button type="submit" class="btn btn-blue3">
                                <span class="las la-search"></span>
                                FIND
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <div class="da-row">
        <div class="da-col-xs-12">
            <div class="suggestions-container">
                <div class="suggestions-text">
                    <p>Suggestions:</p>
                </div>
                <div class="suggestions-pills">
                    <span class="suggestion-pill">Android</span>
                    <span class="suggestion-pill">MySQL</span>
                    <span class="suggestion-pill">Python</span>
                    <span class="suggestion-pill">HTML/CSS</span>
                    <span class="suggestion-pill">Flask</span>
                    <span class="suggestion-pill">API</span>
                    <span class="suggestion-pill">CyberSec</span>
                    <span class="suggestion-pill">Data Science</span>
                </div>
            </div>
        </div>
    </div>

    <div class="da-row">
        <div class="search-result-controls">
            <div class="search-result-controls-left">
                <span>Showing 0 Job Results</span>
                <span>Based on your preferences</span>
            </div>
            <div class="search-result-controls-right">
                <form action="">
                    @csrf
                    <input name="fulltime" id="fulltime" type="radio" >
                    <label for="fulltime">Full time</label>
                    <input name="parttime" id="parttime" type="radio">
                    <label for="parttime">Part time</label>
                    <input name="remote" id="remote"  type="radio">
                    <label for="remote">Remote</label>
                    <select name="time-filter" id="">
                        <option value=""> Newest</option>
                    </select>
                </form>
            </div>
        </div>
    </div>
{{--
    //da_hustle
    /public_html/da_hustle
     --}}
    <div class="da-row">
        @if (!isset($jobs))
            <p>Search to find Jobs</p>
        @else
            @foreach ($jobs as $job)
            <div class="da-col-xs-12 da-col-sm-6 da-col-md-4 da-col-lg-4">
                <div class="dash-card">
                    <div class="search-result-card">
                        <div class="search-result-card-header">
                            <div class="search-result-card-header-left">
                                <span>{{ $job->company->company_name }}</span>
                                <span>{{ $job['job_title'] }}</span>
                                <span>{{ $job->salaryrange->salary_range }}</span>
                            </div>
                            <div class="search-result-card-header-right">
                                <div class="search-result-card-header-company-logo">
                                    <img src="{{ asset('assets/company_logos/'.$job->company->company_logo) }}" alt="">
                                </div>
                            </div>
                        </div>
                        <div class="search-result-card-body">
                            <p>
                                {{ $job['job_description'] }}
                            </p>
                        </div>
                        <div class="search-result-card-footer">
                            <span>{{ $job->jobtype->jobtype_name }}</span>
                            <span>{{ $job->joblocation->location_name }}</span>
                        </div>
                        <div class="search-result-card-foot">
                            <a href="#" class="btn btn-blue2">View</a>
                        </div>
                    </div>
                </div>
            </div>
            @endforeach
        @endif
    </div>

</div>

